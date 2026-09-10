from organization.store import DomainError
from tests.test_returns import ReturnTests


class ReturnReview(ReturnTests):
    def test_no_failure_without_return_and_no_duplicate_return(self):
        self.task()
        self.execution()
        with self.assertRaises(DomainError): self.call('fail', {'execution_id':'E1'})
        self.assertEqual(self.org.store.state()['Execution']['E1']['status'], 'running')
        self.returned()
        with self.assertRaises(DomainError): self.returned()

    def test_review_does_not_imply_acceptance_or_selection(self):
        self.task()
        self.execution()
        self.returned()
        self.call('review', {'id':'V1','return_id':'R1','credible':True,'evidence':'Fixture review'}, 'H2')
        self.assertNotIn('Acceptance', self.org.store.state())
        with self.assertRaises(DomainError): self.call('select', {'id':'SEL','task_id':'T1','return_id':'R1','rationale':'Skipping acceptance'}, 'H3')
        with self.assertRaises(DomainError): self.call('accept', {'id':'C1','return_id':'R1','review_id':'V1','accepted':True,'rationale':'Wrong authority'}, 'H2')

    def test_failed_untrusted_and_cross_result_acceptance_rejected(self):
        self.task()
        self.execution()
        self.returned(command='fail')
        self.call('review', {'id':'V1','return_id':'R1','credible':True,'evidence':'Failure verified'}, 'H2')
        with self.assertRaises(DomainError): self.call('accept', {'id':'C1','return_id':'R1','review_id':'V1','accepted':True,'rationale':'Invalid success claim'})
        self.execution(2)
        self.returned(2)
        with self.assertRaises(DomainError): self.call('accept', {'id':'C2','return_id':'R2','review_id':'V1','accepted':True,'rationale':'Wrong review'})

    def test_annotations_cannot_silently_change_reviewed_facts(self):
        self.task()
        self.execution()
        self.returned()
        self.accepted()
        with self.assertRaises(DomainError): self.call('annotate_return', {'return_id':'R1','action':'correct','text':'Changed after acceptance'})
