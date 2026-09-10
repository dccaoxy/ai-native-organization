"""Agent enrollment is a proposal; a Human grants delegation separately."""
from organization.core import require
from organization.store import DomainError


def handle(s, command, data):
    if command == 'register_agent':
        require(data, ['id','name','version','capabilities'])
        if s.actor != 'AGENT_GATEWAY':
            raise DomainError('Gateway registration path required', 403)
        s.new('AgentRegistration', data['id'])
        s.emit('AgentRegistration', {**data, 'status':'pending', 'human_id':'none',
               'hau_id':'none', 'agent_id':'none', 'permissions':[], 'allowed_tasks':[]},
               'AgentRegistered', 'agent enrollment; no execution authority')
    elif command == 'approve_agent':
        require(data, ['registration_id','hau_id','permissions','allowed_tasks'])
        reg = s.get('AgentRegistration', data['registration_id'])
        owner = s.human()['id']
        if reg['status'] != 'pending':
            raise DomainError('Registration already decided', 409)
        if not isinstance(data['allowed_tasks'], list) or not data['allowed_tasks']:
            raise DomainError('Explicit task allowlist required')
        for tid in data['allowed_tasks']:
            s.get('Task', tid)
        agent_id = 'AG-' + reg['id']
        s.handle('bind_agent', {'hau_id':data['hau_id'], 'agent_id':agent_id, 'permissions':data['permissions']})
        reg.update(status='approved', human_id=owner, hau_id=data['hau_id'],
                   agent_id=agent_id, permissions=data['permissions'], allowed_tasks=data['allowed_tasks'])
        s.emit('AgentRegistration', reg, 'AgentRegistrationApproved', 'Human:' + owner, owner)
    elif command == 'revoke_agent':
        require(data, ['registration_id'])
        reg = s.get('AgentRegistration', data['registration_id'])
        auth = s.authority(reg['human_id'])
        if reg['status'] != 'approved':
            raise DomainError('Only approved registration can be revoked', 409)
        agent = s.get('RepresentativeAgent', reg['agent_id'])
        if agent['active'] and s.get('HAU', reg['hau_id'])['agent_id'] == agent['id']:
            s.handle('agent_status', {'agent_id':agent['id'], 'runtime_status':'offline'})
        reg['status'] = 'revoked'
        s.emit('AgentRegistration', reg, 'AgentRegistrationRevoked', auth, reg['human_id'])
