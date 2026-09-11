import secrets
import unittest
from organization.agent_gateway import Gateway
from organization.store import DomainError
from tests import test_learning as learning


class LearningGatewayTests(unittest.TestCase):
    def setUp(self):
        self.fixture=learning.LearningTests();self.fixture.setUp();self.fixture.sources();self.fixture.propose();self.fixture.evidence(1);self.fixture.evidence(2);self.fixture.verify()
        self.key=secrets.token_urlsafe(32);self.g=Gateway(self.fixture.org.store.path,self.key)
        self.token=secrets.token_urlsafe(32)
        self.g.dispatch('POST','/v1/agents/register',self.token,{'id':'learning-agent','name':'Synthetic','version':'1','capabilities':['knowledge']})

    def tearDown(self):self.fixture.tearDown()

    def approve(self,tasks,permissions):
        self.g.dispatch('POST','/control/commands',self.key,{'actor':'H3','command':'approve_agent','data':{'registration_id':'learning-agent','hau_id':'U3','permissions':permissions,'allowed_tasks':tasks},'idempotency_key':'approve'})

    def test_pending_and_out_of_scope_knowledge_not_exposed(self):
        with self.assertRaises(DomainError):self.g.dispatch('GET','/v1/knowledge',self.token,None)
        self.approve(['T1'],['claim'])
        self.assertEqual(self.g.dispatch('GET','/v1/knowledge',self.token,None)['knowledge'],[])

    def test_projection_hides_evidence_and_use_needs_delegation(self):
        self.approve(['T2'],['claim'])
        k=self.g.dispatch('GET','/v1/knowledge',self.token,None)['knowledge'][0]
        self.assertEqual(k['task_ids'],['T2']);self.assertNotIn('evidence_ids',k);self.assertNotIn('snapshot',k)
        with self.assertRaises(DomainError):self.g.dispatch('POST','/v1/commands',self.token,{'command':'use_knowledge','data':{'id':'U','execution_id':'E3','knowledge_id':'K1','decision':'adopted','reason':'test','package_id':'none'},'idempotency_key':'no-delegation'})
