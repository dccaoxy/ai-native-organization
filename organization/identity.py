from organization.core import require
from organization.contracts import CONTRACT, validate
from organization.store import DomainError

DELEGABLE = {'claim','ack','progress','blocked','escalate','resume','request_boundary','submit','fail','release'}


def interrupt(s, execution, authority):
    s.transition(execution, 'interrupt')
    s.emit('Execution', execution, 'ExecutionInterrupted', authority,
           execution['accountable_owner'], execution['task_id'])


def handle(s, command, data):
    if command == 'register_human':
        require(data, ['id','display_name'])
        if s.actor != 'SIMULATOR': raise DomainError('Simulation bootstrap authority required', 403)
        s.new('Human', data['id'])
        if data['id'] == 'SIMULATOR' or data['id'] in s.state.get('RepresentativeAgent', {}):
            raise DomainError('Reserved or ambiguous actor identity', 409)
        s.emit('Human', {**data,'kind':'human'}, 'HumanRegistered', 'simulation bootstrap; no real identity claim')
    elif command == 'bind_agent':
        require(data, ['hau_id','agent_id','permissions'])
        human = s.human()['id']
        if not isinstance(data['permissions'], list) or any(not isinstance(p, str) for p in data['permissions']):
            raise DomainError('Permissions must be an explicit string list')
        if not set(data['permissions']).issubset(DELEGABLE): raise DomainError('Human-only authority cannot be delegated in M01', 403)
        if data['agent_id'] == 'SIMULATOR' or data['agent_id'] in s.state.get('Human', {}): raise DomainError('Ambiguous actor identity', 409)
        for hau in s.state.get('HAU', {}).values():
            if hau['human_id'] == human and hau['id'] != data['hau_id']:
                raise DomainError('One stable HAU identity per Human in M01', 409)
            if hau['id'] == data['hau_id'] and hau['human_id'] != human:
                raise DomainError('Cannot take another Human HAU', 403)
        for agent in list(s.state.get('RepresentativeAgent', {}).values()):
            if agent['id'] == data['agent_id'] and agent['human_id'] != human:
                raise DomainError('Agent identity already represents another Human', 403)
            if agent['human_id'] == human and agent['active']:
                previous = dict(agent, active=False)
                s.emit('RepresentativeAgent', previous, 'AgentBound', 'Human:' + human, human)
        obj = {'id':data['agent_id'],'human_id':human,'hau_id':data['hau_id'],
               'active':True,'permissions':data['permissions'],'runtime_status':'online'}
        s.emit('RepresentativeAgent', obj, 'AgentBound', 'Human:' + human, human)
        s.emit('HAU', {'id':data['hau_id'],'human_id':human,'agent_id':obj['id']}, 'AgentBound', 'Human:' + human, human)
    elif command == 'agent_status':
        require(data, ['agent_id','runtime_status'])
        agent = s.get('RepresentativeAgent', data['agent_id'])
        hau = s.get('HAU', agent['hau_id'])
        if s.actor != agent['human_id'] and s.actor != agent['id']: raise DomainError('Cannot change foreign Agent runtime', 403)
        if not agent['active'] or hau['agent_id'] != agent['id']: raise DomainError('Inactive Agent interface', 403)
        agent['runtime_status'] = data['runtime_status']
        validate('RepresentativeAgent', agent)
        auth = 'Human:' + agent['human_id'] + '/runtime:' + s.actor
        s.emit('RepresentativeAgent', agent, 'AgentStatusChanged', auth, agent['human_id'])
        if agent['runtime_status'] == 'offline':
            for execution in list(s.state.get('Execution', {}).values()):
                if execution['hau_id'] == hau['id'] and execution['status'] in ('claimed','running','blocked'):
                    interrupt(s, dict(execution), auth)
    elif command == 'sweep':
        require(data, [])
        if s.actor != 'SIMULATOR': raise DomainError('Control-plane sweep authority required', 403)
        for execution in list(s.state.get('Execution', {}).values()):
            status = execution['status']
            if status not in ('claimed','running','blocked'): continue
            parameter = 'ack_timeout_seconds' if status == 'claimed' else 'progress_timeout_seconds'
            timeout = CONTRACT['parameters'][parameter]['default']
            if s.now - execution['last_seen'] >= timeout:
                interrupt(s, dict(execution), 'simulation-control-plane/' + parameter + '=' + str(timeout))
