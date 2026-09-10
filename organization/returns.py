from organization.core import require
from organization.store import DomainError
from organization.work import pending


def handle(s, command, data):
    if command in ('submit','fail','release'):
        require(data, ['id','execution_id','result','observed_terrain','major_execution_facts','reflection'])
        s.new('Return', data['id'])
        execution = s.get('Execution', data['execution_id'])
        auth = s.executor(execution, command)
        if execution['return_id'] != 'none': raise DomainError('Execution already has a formal Return', 409)
        s.transition(execution, command)
        result = {**data,'outcome':{'submit':'success','fail':'failure','release':'released'}[command], 'human_annotations':[]}
        s.emit('Return', result, {'submit':'ResultSubmitted','fail':'ExecutionFailed','release':'ExecutionReleased'}[command],
               auth, execution['accountable_owner'], execution['task_id'])
        execution['return_id'] = result['id']
        s.attach('Execution', execution)
        for request in pending(s, execution['id']):
            request = dict(request, status='cancelled')
            s.emit('BoundaryRequest', request, 'BoundaryCancelled', auth, execution['accountable_owner'], execution['task_id'])
        if command in ('fail','release'):
            s.transition(execution, 'close')
            s.emit('Execution', execution, 'ExecutionClosed', auth, execution['accountable_owner'], execution['task_id'])
    elif command == 'annotate_return':
        require(data, ['return_id','action','text'])
        result = s.get('Return', data['return_id'])
        execution = s.get('Execution', result['execution_id'])
        auth = s.authority(execution['accountable_owner'])
        if data['action'] not in ('confirm','correct','add') or not isinstance(data['text'], str) or not data['text'].strip():
            raise DomainError('Explicit Human Confirm/Correct/Add text required')
        if any(r['return_id'] == result['id'] for r in s.state.get('Review', {}).values()):
            raise DomainError('Reviewed Return is immutable in M01; use a separately reviewed change proposal', 409)
        result['human_annotations'].append(data['action'] + ': ' + data['text'])
        s.emit('Return', result, 'ReturnAnnotated', auth, execution['accountable_owner'], execution['task_id'])
    elif command == 'review':
        require(data, ['id','return_id','credible','evidence'])
        s.new('Review', data['id'])
        result = s.get('Return', data['return_id'])
        execution = s.get('Execution', result['execution_id'])
        task = s.get('Task', execution['task_id'])
        auth = s.authority(task['review_authority'])
        if any(r['return_id'] == result['id'] for r in s.state.get('Review', {}).values()):
            raise DomainError('Review is immutable; new outcome needs a new attempt', 409)
        s.emit('Review', {**data,'reviewer':s.actor}, 'ResultReviewed', auth, execution['accountable_owner'], task['id'])
    elif command == 'accept':
        require(data, ['id','return_id','review_id','accepted','rationale'])
        s.new('Acceptance', data['id'])
        result = s.get('Return', data['return_id'])
        review = s.get('Review', data['review_id'])
        execution = s.get('Execution', result['execution_id'])
        task = s.get('Task', execution['task_id'])
        auth = s.authority(task['acceptance_authority'])
        if review['return_id'] != result['id']: raise DomainError('Review belongs to a different Return', 409)
        if any(a['return_id'] == result['id'] for a in s.state.get('Acceptance', {}).values()):
            raise DomainError('Acceptance is immutable; new outcome needs a new attempt', 409)
        if data['accepted'] is True and (not review['credible'] or result['outcome'] != 'success'):
            raise DomainError('Cannot accept an untrusted, failed or released Result', 409)
        s.emit('Acceptance', {**data,'acceptor':s.actor}, 'ResultAccepted' if data['accepted'] else 'ResultRejected',
               auth, execution['accountable_owner'], task['id'])
        if execution['status'] != 'closed':
            s.transition(execution, 'close')
            s.emit('Execution', execution, 'ExecutionClosed', auth, execution['accountable_owner'], task['id'])
    elif command == 'select':
        require(data, ['id','task_id','return_id','rationale'])
        s.new('Selection', data['id'])
        task = s.get('Task', data['task_id'])
        auth = s.authority(task['selection_authority'])
        result = s.get('Return', data['return_id'])
        execution = s.get('Execution', result['execution_id'])
        if task['status'] != 'published' or execution['task_id'] != task['id']:
            raise DomainError('Result cannot be selected for this Task', 409)
        if not any(a['return_id'] == result['id'] and a['accepted'] for a in s.state.get('Acceptance', {}).values()):
            raise DomainError('Selection requires an accepted Result', 409)
        s.emit('Selection', {**data,'selector':s.actor}, 'ResultSelected', auth, execution['accountable_owner'], task['id'])
        task['status'] = 'closed'
        s.attach('Task', task)
