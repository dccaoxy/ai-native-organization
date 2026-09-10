from organization.store import DomainError
from tests.test_work import WorkTests


class WorkReview(WorkTests):
    def test_no_agent_or_wrong_human_can_expand_boundary(self):
        self.task()
        self.execution()
        self.request()
        for actor in ('A1','H2'):
            with self.assertRaises(DomainError): self.call('decide_boundary', {'request_id':'B1','decision':'approved'}, actor)
        with self.assertRaises(DomainError): self.call('resume', {'execution_id':'E1','summary':'Try skipping approval'})
        self.assertEqual(self.org.store.state()['Execution']['E1']['runtime_boundary'], ['read'])

    def test_private_workspace_not_required_or_collected(self):
        self.task()
        self.execution()
        self.call('progress', {'execution_id':'E1','summary':'Public delivery checkpoint'})
        with self.assertRaises(DomainError): self.call('progress', {'execution_id':'E1','summary':'Public','private_thought':'not organizational evidence'})
        self.assertNotIn('private_thought', str(self.org.store.events()))

    def test_cannot_repeat_boundary_decision_or_cross_accountability(self):
        self.task()
        self.execution()
        self.request()
        self.call('decide_boundary', {'request_id':'B1','decision':'approved'})
        with self.assertRaises(DomainError): self.call('decide_boundary', {'request_id':'B1','decision':'rejected'})
        with self.assertRaises(DomainError): self.call('progress', {'execution_id':'E1','summary':'Foreign update'}, 'H2')
