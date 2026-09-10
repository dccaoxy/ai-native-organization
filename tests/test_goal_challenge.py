from pathlib import Path
import tempfile
import unittest
from organization.core import Organization
from organization.goals import revision
from organization.scale_simulation import scenario
from organization.store import DomainError, Store
from tests import test_http


def open_work(send):
    scenario(send, tasks=1)
    send(actor='H0', command='create_task', data={'id':'open', 'primary_goal':'G0', 'expected_output':'Synthetic output', 'acceptance_criteria':'Existing task contract', 'boundary':['read'], 'execution_mode':'parallel', 'review_authority':'H8', 'acceptance_authority':'H0', 'selection_authority':'H9'}, idempotency_key='open')
    send(actor='H0', command='publish', data={'task_id':'open'}, idempotency_key='publish-open')
    send(actor='A1', command='claim', data={'id':'live', 'task_id':'open', 'hau_id':'U1'}, idempotency_key='live')
    send(actor='A1', command='ack', data={'execution_id':'live'}, idempotency_key='live-ack')


def proposal(identifier='Q1', component='success_criteria'):
    return {'id':identifier, 'goal_id':'G0', 'component':component, 'proposed_value':'Explicit revised synthetic criterion', 'evidence':'Synthetic outcome exposes missing criterion', 'reason':'Correct the smallest component', 'expected_revision':0}


def decision(identifier='D1', challenge='Q1', outcome='modify'):
    return {'id':identifier, 'challenge_id':challenge, 'decision':outcome, 'expected_revision':0, 'reason':'Human fixture judgment', 'evidence':'Inspected synthetic evidence'}


class GoalChallengeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / 'goal.sqlite3'
        self.org = Organization(self.path)
        open_work(self.org.execute)

    def call(self, actor, command, data, key):
        return self.org.execute(actor, command, data, key)

    def test_challenge_does_not_mutate_goal_or_pause_any_work(self):
        before = self.org.store.state()
        self.call('A1', 'challenge_goal', proposal(), 'q')
        after = self.org.store.state()
        for kind in ('Goal','Task','Execution','Return'):
            self.assertEqual(after[kind], before[kind])
        self.assertEqual(after['GoalChallenge']['Q1']['status'], 'pending')

    def test_human_modify_versions_diff_impacts_and_replay(self):
        before = self.org.store.state()
        self.call('A1','challenge_goal',proposal(),'q')
        result = self.call('H0','decide_goal_challenge',decision(),'d')
        self.assertEqual(self.call('H0','decide_goal_challenge',decision(),'d'), result)
        after = self.org.store.state()
        change = after['GoalRevision']['D1/revision']
        self.assertEqual(change['version'], 1)
        self.assertEqual(change['before'], before['Goal']['G0'])
        self.assertEqual(change['after'], after['Goal']['G0'])
        self.assertEqual(change['affected_tasks'], ['open'])
        self.assertEqual(change['affected_executions'], ['live'])
        for kind in ('Task','Execution','Return','Acceptance','Selection'):
            self.assertEqual(before[kind], after[kind])
        self.assertEqual(Organization(self.path).store.state(), after)
        self.assertEqual(Store.replay(self.org.store.events()), after)

    def test_keep_closes_challenge_without_revision(self):
        self.call('H1','challenge_goal',proposal(),'q')
        before = self.org.store.state()['Goal']
        self.call('H0','decide_goal_challenge',decision(outcome='keep'),'d')
        state = self.org.store.state()
        self.assertEqual(state['Goal'], before)
        self.assertEqual(revision(state, 'G0'), 0)
        self.assertEqual(state['GoalChallenge']['Q1']['status'], 'decided')

    def test_agent_and_foreign_human_cannot_decide(self):
        self.call('A1','challenge_goal',proposal(),'q')
        before = self.org.store.events()
        for actor in ('A1','H1'):
            with self.assertRaises(DomainError):
                self.call(actor,'decide_goal_challenge',decision(),'bad-'+actor)
        self.assertEqual(self.org.store.events(), before)

    def test_stale_competing_challenge_and_double_decision_rejected(self):
        for i in (1,2):
            self.call('H1','challenge_goal',proposal('Q'+str(i)),'q'+str(i))
        self.call('H0','decide_goal_challenge',decision(),'d')
        before = self.org.store.events()
        for data in (decision('D2','Q2'), decision('D3','Q1')):
            with self.assertRaises(DomainError):
                self.call('H0','decide_goal_challenge',data,data['id'])
        self.assertEqual(self.org.store.events(), before)

    def test_boundary_authority_not_inferred_from_goal_owner(self):
        self.call('H1','challenge_goal',proposal(component='boundary'),'q')
        before = self.org.store.events()
        with self.assertRaises(DomainError):
            self.call('H0','decide_goal_challenge',decision(),'d')
        self.assertEqual(self.org.store.events(), before)

    def test_invalid_evidence_rolls_back_entire_decision(self):
        self.call('H1','challenge_goal',proposal(),'q')
        before = self.org.store.events()
        with self.assertRaises(ValueError):
            self.call('H0','decide_goal_challenge',dict(decision(), evidence=''),'d')
        self.assertEqual(self.org.store.events(), before)

    def test_offline_agent_cannot_challenge(self):
        self.call('H1','agent_status',{'agent_id':'A1','runtime_status':'offline'},'offline')
        before = self.org.store.events()
        with self.assertRaises(DomainError):
            self.call('A1','challenge_goal',proposal(),'q')
        self.assertEqual(self.org.store.events(), before)


class GoalChallengeHTTPTests(unittest.TestCase):
    setUp = test_http.HTTPTests.setUp
    tearDown = test_http.HTTPTests.tearDown
    request = test_http.HTTPTests.request

    def test_goal_challenge_through_real_http(self):
        send = lambda **body: self.request('/api/commands', body)
        open_work(send)
        send(actor='A1', command='challenge_goal', data=proposal(), idempotency_key='q')
        send(actor='H0', command='decide_goal_challenge', data=decision(), idempotency_key='d')
        state = self.request('/api/state')['state']
        self.assertEqual(state['GoalRevision']['D1/revision']['version'], 1)
        self.assertEqual(state['Execution']['live']['status'], 'running')
