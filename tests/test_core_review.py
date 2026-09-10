from organization.store import DomainError
from tests.test_core import CoreTests


class CoreReview(CoreTests):
    def test_goal_authority_cannot_be_impersonated_by_agent(self):
        with self.assertRaises(DomainError):
            self.call('activate_goal', {'id':'G1','desired_change':'x','success_criteria':'y','boundary':['read'],'goal_authority':'H1'}, 'A1')
        self.assertNotIn('Goal', self.org.store.state())

    def test_unpublished_and_foreign_claims_rejected(self):
        self.task()
        with self.assertRaises(DomainError): self.call('claim', {'id':'E1','task_id':'T1','hau_id':'U2'}, 'H1')
        with self.assertRaises(DomainError): self.call('ack', {'execution_id':'missing'})
        self.execution()
        with self.assertRaises(DomainError): self.call('ack', {'execution_id':'E1'})

    def test_task_boundary_cannot_exceed_goal(self):
        self.task()
        bad = dict(self.org.store.state()['Task']['T1'])
        bad.pop('status')
        bad.update(id='T2',boundary=['company-admin'])
        with self.assertRaises(DomainError): self.call('create_task', bad)

    def test_real_mode_is_not_silently_enabled(self):
        from organization.core import Organization
        with self.assertRaises(DomainError) as caught: Organization('unused.sqlite3', simulation=False)
        self.assertEqual(caught.exception.status, 503)
