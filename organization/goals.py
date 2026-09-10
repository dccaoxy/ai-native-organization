"""Evidence-based Goal challenge; only its Human authority can decide changes."""
from organization.core import require
from organization.store import DomainError


def revision(state, goal_id):
    return max((r['version'] for r in state.get('GoalRevision', {}).values() if r['goal_id'] == goal_id), default=0)


def handle(s, command, data):
    if command == 'challenge_goal':
        require(data, ['id', 'goal_id', 'component', 'proposed_value', 'evidence', 'reason', 'expected_revision'])
        goal = s.get('Goal', data['goal_id'])
        s.new('GoalChallenge', data['id'])
        if s.actor in s.state.get('Human', {}):
            owner = s.human()['id']
            authority = 'Human:' + owner
        else:
            agent = s.get('RepresentativeAgent', s.actor)
            authority = s.hau_actor(s.get('HAU', agent['hau_id']), 'challenge_goal')
            owner = agent['human_id']
        current = revision(s.state, goal['id'])
        if type(data['expected_revision']) is not int or data['expected_revision'] != current:
            raise DomainError('Goal revision changed; refresh evidence before challenging', 409)
        if goal['status'] != 'active':
            raise DomainError('This engineering slice challenges active Goals only', 409)
        obj = {**data, 'challenger': s.actor, 'status': 'pending'}
        s.emit('GoalChallenge', obj, 'GoalChallenged', authority, owner, goal['id'])
    elif command == 'decide_goal_challenge':
        require(data, ['id', 'challenge_id', 'decision', 'expected_revision', 'reason', 'evidence'])
        s.new('GoalDecision', data['id'])
        challenge = s.get('GoalChallenge', data['challenge_id'])
        goal = s.get('Goal', challenge['goal_id'])
        authority = s.authority(goal['goal_authority'])
        current = revision(s.state, goal['id'])
        if (type(data['expected_revision']) is not int or data['expected_revision'] != current or
                challenge['expected_revision'] != current or challenge['status'] != 'pending'):
            raise DomainError('Stale Goal revision or challenge already decided', 409)
        if data['decision'] not in ('keep', 'modify'):
            raise DomainError('Only Keep or component Modify implemented; other lifecycle decisions require separate engineering')
        affected_tasks, affected_executions = [], []
        if data['decision'] == 'modify':
            component = challenge['component']
            if component not in ('desired_change', 'success_criteria'):
                raise DomainError('Boundary/risk and other components require their own authority-aware change contract', 409)
            if goal[component] == challenge['proposed_value']:
                raise DomainError('No material difference; use Keep', 409)
            before = dict(goal)
            goal[component] = challenge['proposed_value']
            affected_tasks = sorted(t['id'] for t in s.state.get('Task', {}).values() if t['primary_goal'] == goal['id'] and t['status'] != 'closed')
            affected_executions = sorted(e['id'] for e in s.state.get('Execution', {}).values() if e['task_id'] in affected_tasks and e['status'] != 'closed')
            rid = data['id'] + '/revision'
            s.new('GoalRevision', rid)
            s.emit('GoalRevision', {'id': rid, 'goal_id': goal['id'], 'version': current + 1,
                   'component': component, 'before': before, 'after': dict(goal),
                   'reason': data['reason'], 'evidence': data['evidence'], 'decision_id': data['id'],
                   'affected_tasks': affected_tasks, 'affected_executions': affected_executions},
                   'GoalRevised', authority, goal['goal_authority'], goal['id'])
            s.attach('Goal', goal)
        s.emit('GoalDecision', {**data, 'goal_id': goal['id'], 'decider': s.actor,
               'resulting_revision': revision(s.state, goal['id']), 'affected_tasks': affected_tasks,
               'affected_executions': affected_executions}, 'GoalChallengeDecided', authority, goal['goal_authority'], goal['id'])
        challenge['status'] = 'decided'
        s.attach('GoalChallenge', challenge)
