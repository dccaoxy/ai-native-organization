import uuid
from organization.core import require
from organization.store import DomainError


def pending(s, execution_id):
    return [r for r in s.state.get('BoundaryRequest', {}).values()
            if r['execution_id'] == execution_id and r['status'] == 'pending']


def handle(s, command, data):
    if command in ('progress','blocked','escalate','resume'):
        require(data, ['execution_id','summary'])
        obj = s.get('Execution', data['execution_id'])
        auth = s.executor(obj, command)
        if command == 'resume' and pending(s, obj['id']):
            raise DomainError('Pending Human Boundary decision; expansion is not authorized', 403)
        s.transition(obj, command)
        s.emit('Execution', obj, {'progress':'Progress','blocked':'Blocked','escalate':'Escalated','resume':'Resumed'}[command],
               auth, obj['accountable_owner'], obj['task_id'])
        s.attach('WorkSignal', {'id':uuid.uuid4().hex,'execution_id':obj['id'],'kind':command,'summary':data['summary']})
    elif command == 'request_boundary':
        require(data, ['id','execution_id','requested_scope','reason'])
        s.new('BoundaryRequest', data['id'])
        obj = s.get('Execution', data['execution_id'])
        auth = s.executor(obj, command)
        if obj['status'] not in ('running','blocked','interrupted'): raise DomainError('Boundary request requires live attempt', 409)
        if pending(s, obj['id']): raise DomainError('Resolve existing Boundary request first', 409)
        task = s.get('Task', obj['task_id'])
        goal = s.get('Goal', task['primary_goal'])
        request = {**data,'authority':goal['goal_authority'],'status':'pending'}
        s.emit('BoundaryRequest', request, 'BoundaryRequested', auth, obj['accountable_owner'], obj['task_id'])
        obj['status'] = 'blocked'
        obj['last_seen'] = s.now
        s.attach('Execution', obj)
    elif command == 'decide_boundary':
        require(data, ['request_id','decision'], ['modified_scope'])
        request = s.get('BoundaryRequest', data['request_id'])
        auth = s.authority(request['authority'])
        if request['status'] != 'pending': raise DomainError('Boundary request already decided', 409)
        obj = s.get('Execution', request['execution_id'])
        if obj['status'] not in ('blocked','interrupted'): raise DomainError('Attempt already returned or closed', 409)
        decision = data['decision']
        if decision not in ('approved','rejected','modified'): raise DomainError('Unknown Boundary decision')
        if decision == 'modified':
            if 'modified_scope' not in data: raise DomainError('Explicit modified scope required')
            request['requested_scope'] = data['modified_scope']
        elif 'modified_scope' in data: raise DomainError('Modified scope only applies to modified decision')
        request['status'] = decision
        s.emit('BoundaryRequest', request, {'approved':'BoundaryApproved','rejected':'BoundaryRejected','modified':'BoundaryModified'}[decision],
               auth, obj['accountable_owner'], obj['task_id'])
        if decision in ('approved','modified'):
            obj['runtime_boundary'] = list(request['requested_scope'])
        # Only this attempt changes. Task shared intent and other Execution
        # boundaries remain unchanged. Human decision does not auto-resume work.
        s.attach('Execution', obj)
