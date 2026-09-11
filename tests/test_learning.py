import json
import unittest
from tests import test_core as core
from organization.store import DomainError,Store


class LearningTests(unittest.TestCase):
    setUp=core.CoreTests.setUp
    tearDown=core.CoreTests.tearDown
    call=core.CoreTests.call
    task=core.CoreTests.task
    execution=core.CoreTests.execution

    def sources(self):
        self.task()
        self.call('create_task',{'id':'T2','primary_goal':'G1','expected_output':'Second synthetic task','acceptance_criteria':'Traceable bounded reuse','boundary':['read'],'execution_mode':'parallel','review_authority':'H2','acceptance_authority':'H1','selection_authority':'H3'})
        self.call('publish',{'task_id':'T2'})
        for i in (1,2):
            self.execution(i)
            self.result(i)

    def result(self,i,fail=False):
        self.call('fail' if fail else 'submit',{'id':f'R{i}','execution_id':f'E{i}','result':'Explicit synthetic result','observed_terrain':'Local fixture','major_execution_facts':'Synthetic protocol actions','reflection':'No real learning efficacy claim'},f'H{i}')
        self.call('review',{'id':f'RV{i}','return_id':f'R{i}','credible':not fail,'evidence':'Fixture trace inspected'},'H2')
        self.call('accept',{'id':f'AC{i}','return_id':f'R{i}','review_id':f'RV{i}','accepted':not fail,'rationale':'Fixture criterion only'},'H1')

    def propose(self,cid='K1',previous='none'):
        return self.call('propose_claim',{'id':cid,'return_id':'R1','reviewer':'H3','previous_id':previous,'core_claim':'Synthetic bounded claim','scope':'Explicit local fixture only','boundary':['read'],'mechanism':'Candidate explanation, no causal proof','transfer_conditions':'Same fixture protocol; not real business','task_ids':['T2']})

    def evidence(self,i,cid='K1',relation='supports',upstream=None):
        return self.call('capture_evidence',{'id':cid+f'/EV{i}','claim_id':cid,'return_id':f'R{i}','relation':relation,'rationale':'Synthetic relation, not empirical evidence','upstream_sources':upstream or [f'fixture-source-{i}']},f'H{i}')

    def verify(self,cid='K1',ids=None):
        return self.call('verify_claim',{'id':cid+'/V','claim_id':cid,'decision':'validated','evidence_ids':ids or [cid+'/EV1',cid+'/EV2'],'falsification':'Checked counterexample fixture','alternatives':'Shared upstream and selection bias considered','limitations':'Synthetic protocol only','independence':'Distinct declared fixture sources, not automatically verified scientific independence'},'H3')

    def ready(self):
        self.sources();self.propose();self.evidence(1);self.evidence(2);self.verify()
        self.call('assemble_route',{'package_id':'route/R1','knowledge_id':'K1','components':{k:'Explicit fixture '+k for k in ['data','tools','agent_configuration','runtime','practice','oversight']}})
        self.call('claim',{'id':'E3','task_id':'T2','hau_id':'U3'},'H3');self.call('ack',{'execution_id':'E3'},'H3')

    def use(self):
        return self.call('use_knowledge',{'id':'USE1','execution_id':'E3','knowledge_id':'K1','decision':'adopted','reason':'Matches explicit synthetic scope','package_id':'route/R1'},'H3')

    def outcome(self,fail=False):
        self.result(3,fail)
        self.call('record_learning_outcome',{'id':'OUT1','use_id':'USE1','return_id':'R3','interpretation':'Association only; no causal assertion'},'H3')

    def test_cross_task_reproduction_and_replay(self):
        self.ready();self.use();self.outcome()
        self.call('record_reproduction',{'id':'REP1','package_id':'route/R1','use_id':'USE1','return_id':'R3'})
        state=self.org.store.state()
        self.assertEqual(state['CapabilityRoute']['route/R1']['status'],'reproduced')
        self.assertEqual(Store.replay(self.org.store.events()),state)
        self.assertEqual(state['Execution']['E3']['accountable_owner'],'H3')
        self.assertEqual(state['Execution']['E3']['runtime_boundary'],['read'])

    def test_single_source_not_generalized_and_no_self_verification(self):
        self.sources();self.propose();self.evidence(1)
        before=len(self.org.store.events())
        with self.assertRaises(DomainError):self.verify(ids=['K1/EV1'])
        self.assertEqual(len(self.org.store.events()),before)
        self.assertEqual(self.org.store.state()['LearningClaim']['K1']['status'],'candidate')
        self.assertEqual(self.org.store.state()['CapabilityRoute']['route/R1']['status'],'candidate')

    def test_shared_upstream_is_not_independence(self):
        self.sources();self.propose();self.evidence(1,upstream=['shared']);self.evidence(2,upstream=['shared'])
        with self.assertRaises(DomainError):self.verify()

    def test_counter_evidence_cannot_be_omitted(self):
        self.sources();self.propose();self.evidence(1);self.evidence(2,relation='contradicts')
        with self.assertRaises(DomainError):self.verify(ids=['K1/EV1'])
        with self.assertRaises(DomainError):self.verify()

    def test_evidence_snapshot_and_duplicate_source(self):
        self.sources();self.propose();self.evidence(1)
        ev=self.org.store.state()['LearningEvidence']['K1/EV1']
        self.assertEqual(ev['snapshot']['return']['id'],'R1')
        self.assertEqual(len(ev['snapshot']['reviews']),1)
        with self.assertRaises(DomainError):self.call('capture_evidence',{'id':'duplicate','claim_id':'K1','return_id':'R1','relation':'supports','rationale':'repeat','upstream_sources':['other']})

    def test_failure_challenges_dependency_without_causal_claim(self):
        self.ready();self.use();self.outcome(True)
        s=self.org.store.state()
        self.assertEqual(s['KnowledgeRevision']['K1']['status'],'challenged')
        self.assertEqual(s['CapabilityRoute']['route/R1']['status'],'stale')
        with self.assertRaises(DomainError):self.call('record_reproduction',{'id':'REP','package_id':'route/R1','use_id':'USE1','return_id':'R3'})

    def test_revision_keeps_history_and_invalidates_package(self):
        self.ready();self.propose('K2','K1');self.evidence(1,'K2');self.evidence(2,'K2');self.verify('K2')
        s=self.org.store.state()
        self.assertEqual(s['KnowledgeRevision']['K1']['status'],'superseded')
        self.assertEqual(s['KnowledgeRevision']['K2']['version'],2)
        self.assertEqual(s['CapabilityRoute']['route/R1']['status'],'stale')
        with self.assertRaises(DomainError):self.use()

    def test_wrong_human_and_wrong_scope_rejected(self):
        self.ready()
        d={'id':'BAD','execution_id':'E3','knowledge_id':'K1','decision':'adopted','reason':'test','package_id':'none'}
        with self.assertRaises(DomainError):self.call('use_knowledge',d,'H1')
        # A live attempt in T1 is outside explicit K1 task scope.
        self.call('claim',{'id':'E4','task_id':'T1','hau_id':'U3'},'H3')
        with self.assertRaises(DomainError):self.call('use_knowledge',{**d,'execution_id':'E4'},'H3')

    def test_outcome_cannot_reference_unrelated_return(self):
        self.ready();self.use()
        with self.assertRaises(DomainError):self.call('record_learning_outcome',{'id':'OUT','use_id':'USE1','return_id':'R1','interpretation':'wrong'})

    def test_agent_cannot_publish_claim(self):
        self.sources()
        with self.assertRaises(DomainError):self.call('propose_claim',{'id':'K','return_id':'R1','reviewer':'H3','previous_id':'none','core_claim':'x','scope':'x','boundary':['read'],'mechanism':'x','transfer_conditions':'x','task_ids':['T2']},'A1')

    def test_idempotent_evidence_replay(self):
        self.sources();self.propose()
        d={'id':'EV','claim_id':'K1','return_id':'R1','relation':'supports','rationale':'test','upstream_sources':['source']}
        self.org.execute('H1','capture_evidence',d,'same-key');n=len(self.org.store.events())
        self.org.execute('H1','capture_evidence',d,'same-key');self.assertEqual(len(self.org.store.events()),n)

    def test_first_success_captures_route_without_claim_or_acceptance(self):
        self.task();self.execution(1)
        self.call('submit',{'id':'R1','execution_id':'E1','result':'Synthetic success','observed_terrain':'fixture','major_execution_facts':'fixture','reflection':'not validated'})
        s=self.org.store.state()
        self.assertEqual(s['CapabilityRoute']['route/R1']['status'],'candidate')
        self.assertNotIn('KnowledgeRevision',s)
        self.assertIn('CapabilityRoute',self.org.store.events()[-1]['changes'])

    def test_self_verification_and_wrong_verifier_denied(self):
        self.sources();self.propose();self.evidence(1);self.evidence(2)
        with self.assertRaises(DomainError):self.call('verify_claim',{'id':'BADV','claim_id':'K1','decision':'validated','evidence_ids':['K1/EV1','K1/EV2'],'falsification':'x','alternatives':'x','limitations':'x','independence':'x'},'H1')
        self.assertNotIn('KnowledgeRevision',self.org.store.state())

    def test_boundary_cannot_expand_from_knowledge(self):
        self.sources()
        self.call('propose_claim',{'id':'K1','return_id':'R1','reviewer':'H3','previous_id':'none','core_claim':'x','scope':'fixture','boundary':['draft'],'mechanism':'x','transfer_conditions':'x','task_ids':['T2']})
        self.evidence(1);self.evidence(2);self.verify()
        self.call('claim',{'id':'E3','task_id':'T2','hau_id':'U3'},'H3')
        with self.assertRaises(DomainError):self.call('use_knowledge',{'id':'USE','execution_id':'E3','knowledge_id':'K1','decision':'adopted','reason':'test','package_id':'none'},'H3')
        self.assertEqual(self.org.store.state()['Execution']['E3']['runtime_boundary'],['read'])
