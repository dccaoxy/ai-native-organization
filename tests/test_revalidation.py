import unittest
from tests import test_learning as learning
from organization.store import DomainError,Store


class RevalidationTests(unittest.TestCase):
    def setUp(self):
        self.f=learning.LearningTests();self.f.setUp();self.f.ready();self.call=self.f.call;self.org=self.f.org
    def tearDown(self):self.f.tearDown()

    def fail(self):self.f.use();self.f.outcome(True)

    def plan(self):
        return self.call('plan_revalidation',{'id':'PLAN','knowledge_id':'K1','task_id':'T3','goal_id':'G1','expected_output':'Synthetic revalidation','acceptance_criteria':'Traceable revised route','boundary':['read'],'review_authority':'H2','acceptance_authority':'H1','selection_authority':'H3','reason':'Explicit synthetic failure feedback'})

    def revision(self,task_ids=None):
        self.call('revise_knowledge',{'id':'K2','return_id':'R1','reviewer':'H3','previous_id':'K1','core_claim':'Narrow synthetic claim','scope':'Revised fixture scope','boundary':['read'],'mechanism':'Revised candidate explanation','transfer_conditions':'Known synthetic failure excluded','task_ids':task_ids or ['T3'],'reason':'Respond to failed fixture and narrow applicability','addressed_triggers':self.org.store.state()['KnowledgeImpact']['impact/K1']['triggers']})
        self.f.evidence(1,'K2');self.f.evidence(2,'K2');self.f.verify('K2')
        self.call('revise_route',{'id':'ROUTE2','previous_package':'route/R1','knowledge_id':'K2','components':{k:'Revised fixture '+k for k in ['data','tools','agent_configuration','runtime','practice','oversight']},'reason':'Use narrowed knowledge and explicit supervision'})

    def reproduce(self):
        self.call('claim',{'id':'E4','task_id':'T3','hau_id':'U3'},'H3');self.call('ack',{'execution_id':'E4'},'H3')
        self.call('use_knowledge',{'id':'USE4','execution_id':'E4','knowledge_id':'K2','decision':'adopted','reason':'Within revised scope','package_id':'ROUTE2'},'H3')
        self.call('submit',{'id':'R4','execution_id':'E4','result':'Synthetic revised outcome','observed_terrain':'New test task','major_execution_facts':'Explicit package adoption','reflection':'Protocol test, no causal claim'},'H3')
        self.call('review',{'id':'RV4','return_id':'R4','credible':True,'evidence':'Synthetic trace'},'H2')
        self.call('accept',{'id':'AC4','return_id':'R4','review_id':'RV4','accepted':True,'rationale':'Fixture only'})
        self.call('record_learning_outcome',{'id':'OUT4','use_id':'USE4','return_id':'R4','interpretation':'No causal inference'},'H3')
        self.call('record_reproduction',{'id':'REP4','package_id':'ROUTE2','use_id':'USE4','return_id':'R4'})

    def test_new_task_revalidation_preserves_invalid_history(self):
        self.fail();self.plan();self.revision()
        self.assertEqual(self.org.store.state()['CapabilityRoute']['ROUTE2']['status'],'candidate')
        self.reproduce();self.call('complete_revalidation',{'plan_id':'PLAN','reproduction_id':'REP4'})
        s=self.org.store.state();self.assertEqual(s['RevalidationPlan']['PLAN']['status'],'passed')
        self.assertEqual(s['KnowledgeRevision']['K1']['status'],'superseded');self.assertEqual(s['CapabilityRoute']['route/R1']['status'],'stale')
        self.assertEqual(s['KnowledgeImpact']['impact/K1']['status'],'resolved');self.assertEqual(Store.replay(self.org.store.events()),s)

    def test_active_adopters_are_listed_without_pausing(self):
        self.call('claim',{'id':'ACTIVE','task_id':'T2','hau_id':'U2'},'H2');self.call('ack',{'execution_id':'ACTIVE'},'H2')
        self.call('use_knowledge',{'id':'ACTIVEUSE','execution_id':'ACTIVE','knowledge_id':'K1','decision':'adopted','reason':'test','package_id':'none'},'H2')
        self.fail();s=self.org.store.state();self.assertIn('ACTIVE',s['KnowledgeImpact']['impact/K1']['execution_ids']);self.assertEqual(s['Execution']['ACTIVE']['status'],'running')

    def test_rejected_use_failure_does_not_invalidate_unused_knowledge(self):
        self.call('use_knowledge',{'id':'USE1','execution_id':'E3','knowledge_id':'K1','decision':'rejected','reason':'Does not fit','package_id':'none'},'H3')
        self.f.outcome(True)
        self.assertEqual(self.org.store.state()['KnowledgeRevision']['K1']['status'],'validated')

    def test_new_revision_cannot_skip_reason(self):
        self.fail();self.plan()
        self.call('propose_claim',{'id':'K2','return_id':'R1','reviewer':'H3','previous_id':'K1','core_claim':'x','scope':'x','boundary':['read'],'mechanism':'x','transfer_conditions':'x','task_ids':['T3']})
        self.f.evidence(1,'K2');self.f.evidence(2,'K2')
        with self.assertRaises(DomainError):self.f.verify('K2')

    def test_no_premature_completion_or_authority_bypass(self):
        self.fail();self.plan();self.revision()
        before=len(self.org.store.events())
        with self.assertRaises(DomainError):self.call('complete_revalidation',{'plan_id':'PLAN','reproduction_id':'missing'})
        with self.assertRaises(DomainError):self.call('revise_route',{'id':'BAD','previous_package':'route/R1','knowledge_id':'K2','components':{},'reason':'test'},'H2')
        self.assertEqual(len(self.org.store.events()),before)

    def test_wrong_new_task_cannot_complete_plan(self):
        self.fail();self.plan();self.revision();self.reproduce()
        self.call('plan_revalidation',{'id':'PLAN2','knowledge_id':'K1','task_id':'OTHER','goal_id':'G1','expected_output':'Other revalidation','acceptance_criteria':'Different task','boundary':['read'],'review_authority':'H2','acceptance_authority':'H1','selection_authority':'H3','reason':'Another scope'})
        with self.assertRaises(DomainError):self.call('complete_revalidation',{'plan_id':'PLAN2','reproduction_id':'REP4'})

    def test_late_issue_invalidates_successor_and_reopens_impact(self):
        self.fail();self.plan();self.revision();self.reproduce();self.call('complete_revalidation',{'plan_id':'PLAN','reproduction_id':'REP4'})
        self.call('report_knowledge_issue',{'id':'LATE','execution_id':'E3','use_id':'USE1','return_id':'R3','reason':'New late observation, not proof of causation'},'H3')
        s=self.org.store.state();self.assertEqual(s['KnowledgeRevision']['K2']['status'],'challenged');self.assertEqual(s['CapabilityRoute']['ROUTE2']['status'],'stale');self.assertEqual(s['KnowledgeImpact']['impact/K1']['status'],'open')

    def test_plan_boundary_expansion_fails_atomically(self):
        self.fail();before=len(self.org.store.events())
        with self.assertRaises(DomainError):self.call('plan_revalidation',{'id':'PLAN','knowledge_id':'K1','task_id':'T3','goal_id':'G1','expected_output':'x','acceptance_criteria':'x','boundary':['admin'],'review_authority':'H2','acceptance_authority':'H1','selection_authority':'H3','reason':'x'})
        self.assertEqual(len(self.org.store.events()),before)

    def test_pending_plan_limits_successor_to_trial_tasks(self):
        self.fail();self.plan();self.revision(['T3','T2'])
        self.call('claim',{'id':'OTHEREXEC','task_id':'T2','hau_id':'U2'},'H2')
        use={'id':'OTHERUSE','execution_id':'OTHEREXEC','knowledge_id':'K2','decision':'adopted','reason':'Check general reuse gate','package_id':'ROUTE2'}
        with self.assertRaises(DomainError):self.call('use_knowledge',use,'H2')
        self.reproduce();self.call('complete_revalidation',{'plan_id':'PLAN','reproduction_id':'REP4'})
        self.call('use_knowledge',use,'H2')
        self.assertEqual(self.org.store.state()['KnowledgeUse']['OTHERUSE']['knowledge_id'],'K2')
