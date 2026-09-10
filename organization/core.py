"""M01 commands execute inside one SQLite transaction, with explicit authority."""
import copy
from organization.contracts import CONTRACT, validate
from organization.store import DomainError, Store


def require(data, required, optional=()):
    if not isinstance(data, dict) or not set(required).issubset(data) or set(data) - set(required) - set(optional):
        raise DomainError('Missing or unexpected public command fields')


class Session:
    def __init__(self, state, actor, now):
        self.state, self.actor, self.now = state, actor, now
        self.emitted = []

    def get(self, kind, identifier):
        if not isinstance(identifier, str): raise DomainError('Identifier must be a string')
        try: return copy.deepcopy(self.state[kind][identifier])
        except KeyError: raise DomainError(kind + ' does not exist', 409)

    def human(self, identifier=None):
        obj = self.get('Human', identifier or self.actor)
        if obj['kind'] != 'human': raise DomainError('Human Authority required', 403)
        return obj

    def authority(self, expected):
        self.human()
        if self.actor != expected: raise DomainError('Actor has no authority over this object', 403)
        return 'Human:' + expected

    def new(self, kind, identifier):
        if not isinstance(identifier, str) or not identifier.strip(): raise DomainError('Nonempty id required')
        if identifier in self.state.get(kind, {}): raise DomainError('Object id already exists', 409)

    def emit(self, kind, obj, event, authority, owner='not-applicable', correlation=None):
        validate(kind, obj)
        if event not in CONTRACT['event_catalog']: raise DomainError('Unknown formal event')
        self.state.setdefault(kind, {})[obj['id']] = copy.deepcopy(obj)
        self.emitted.append({'type':event,'authority':authority,'owner':owner,
                             'correlation':correlation or obj['id'],
                             'changes':{kind:{obj['id']:copy.deepcopy(obj)}}})

    def hau_actor(self, hau, action):
        owner = self.human(hau['human_id'])['id']
        if self.actor == owner: return 'Human:' + owner
        agent = self.get('RepresentativeAgent', self.actor)
        if not (agent['active'] and agent['runtime_status'] == 'online' and
                hau['agent_id'] == agent['id'] and agent['human_id'] == owner and
                agent['hau_id'] == hau['id'] and action in agent['permissions']):
            raise DomainError('Agent not active or outside explicit delegation', 403)
        return 'Human:' + owner + '/RepresentativeAgent:' + agent['id'] + '/' + action

    def attach(self, kind, obj):
        """Additional changed object belonging to the same formal fact/event."""
        validate(kind, obj)
        self.state.setdefault(kind, {})[obj['id']] = copy.deepcopy(obj)
        self.emitted[-1]['changes'].setdefault(kind, {})[obj['id']] = copy.deepcopy(obj)

    def executor(self, execution, action):
        hau = self.get('HAU', execution['hau_id'])
        if hau['human_id'] != execution['accountable_owner']:
            raise DomainError('Accountability cannot be silently rebound', 409)
        return self.hau_actor(hau, action)

    def transition(self, execution, action):
        rule = CONTRACT['state_machines']['Execution'][action]
        if execution['status'] not in rule['from']: raise DomainError('Invalid Execution transition', 409)
        execution['status'] = rule['to']
        execution['last_seen'] = self.now

    def handle(self, command, data):
        if command == 'activate_goal':
            require(data, ['id','desired_change','success_criteria','boundary','goal_authority'])
            self.new('Goal', data['id'])
            auth = self.authority(data['goal_authority'])
            self.emit('Goal', {**data,'status':'active'}, 'GoalActivated', auth)
        elif command == 'create_task':
            require(data, ['id','primary_goal','expected_output','acceptance_criteria','boundary','execution_mode','review_authority','acceptance_authority','selection_authority'])
            self.new('Task', data['id'])
            goal = self.get('Goal', data['primary_goal'])
            auth = self.authority(goal['goal_authority'])
            if goal['status'] != 'active': raise DomainError('Task requires Active Goal', 409)
            validate('Task', {**data,'status':'draft'})
            if not set(data['boundary']).issubset(goal['boundary']): raise DomainError('Task cannot expand Goal boundary', 403)
            for field in ('review_authority','acceptance_authority','selection_authority'): self.human(data[field])
            self.emit('Task', {**data,'status':'draft'}, 'TaskCreated', auth, correlation=goal['id'])
        elif command == 'publish':
            require(data, ['task_id'])
            task = self.get('Task', data['task_id'])
            goal = self.get('Goal', task['primary_goal'])
            auth = self.authority(goal['goal_authority'])
            if task['status'] != 'draft' or goal['status'] != 'active': raise DomainError('Cannot publish in this state', 409)
            task['status'] = 'published'
            self.emit('Task', task, 'TaskPublished', auth)
        elif command == 'claim':
            require(data, ['id','task_id','hau_id'])
            self.new('Execution', data['id'])
            task = self.get('Task', data['task_id'])
            goal = self.get('Goal', task['primary_goal'])
            if task['status'] != 'published' or goal['status'] != 'active': raise DomainError('Task not claimable', 409)
            hau = self.get('HAU', data['hau_id'])
            auth = self.hau_actor(hau, 'claim')
            obj = {**data,'accountable_owner':hau['human_id'],'status':'claimed',
                   'runtime_boundary':list(task['boundary']),'claimed_at':self.now,'last_seen':self.now,'return_id':'none'}
            self.emit('Execution', obj, 'ExecutionClaimed', auth, hau['human_id'], task['id'])
        elif command == 'ack':
            require(data, ['execution_id'])
            obj = self.get('Execution', data['execution_id'])
            auth = self.executor(obj, command)
            self.transition(obj, 'ack')
            self.emit('Execution', obj, 'ACK', auth, obj['accountable_owner'], obj['task_id'])
        else:
            if command in ('register_human','bind_agent','agent_status','sweep'):
                from organization.identity import handle
            elif command in ('progress','blocked','escalate','resume','request_boundary','decide_boundary'):
                from organization.work import handle
            elif command in ('submit','fail','release','annotate_return','review','accept','select'):
                from organization.returns import handle
            else: raise DomainError('Unknown command')
            handle(self, command, data)
        return self.emitted


class Organization:
    def __init__(self, path, simulation=True, clock=None):
        if simulation is not True:
            raise DomainError('HUMAN_DECISION_REQUIRED: authenticated real identities, data, risk and platform permissions', 503)
        self.store = Store(path, **({'clock':clock} if clock else {}))

    def execute(self, actor, command, data, idempotency_key):
        if not isinstance(actor, str) or not actor.strip() or not isinstance(command, str):
            raise DomainError('Actor and command must be nonempty strings')
        return self.store.transact(actor, command, data, idempotency_key,
            lambda state:Session(state, actor, self.store.clock()).handle(command, data))
