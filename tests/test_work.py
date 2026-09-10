from tests.test_core import CoreTests


class WorkTests(CoreTests):
    def request(self):
        self.call('request_boundary', {'id':'B1','execution_id':'E1','requested_scope':['read','draft'],'reason':'Simulation needs an additional permitted draft operation'})

    def test_boundary_approval_changes_only_one_attempt(self):
        self.task()
        self.execution(1)
        self.execution(2)
        self.request()
        self.assertEqual(self.org.store.state()['Execution']['E1']['runtime_boundary'], ['read'])
        self.call('decide_boundary', {'request_id':'B1','decision':'approved'})
        self.call('resume', {'execution_id':'E1','summary':'Approved boundary received'})
        state = self.org.store.state()
        self.assertEqual(state['Execution']['E1']['runtime_boundary'], ['read','draft'])
        self.assertEqual(state['Execution']['E2']['runtime_boundary'], ['read'])
        self.assertEqual(state['Task']['T1']['boundary'], ['read'])

    def test_rejection_modified_scope_and_formal_signals(self):
        self.task()
        self.execution()
        self.call('progress', {'execution_id':'E1','summary':'Public checkpoint reached'})
        self.call('blocked', {'execution_id':'E1','summary':'Needs authority decision'})
        self.call('escalate', {'execution_id':'E1','summary':'Need help from responsible Human'})
        self.request()
        self.call('decide_boundary', {'request_id':'B1','decision':'rejected'})
        self.call('resume', {'execution_id':'E1','summary':'Continue within original scope'})
        self.assertEqual(self.org.store.state()['Execution']['E1']['runtime_boundary'], ['read'])
        self.call('request_boundary', {'id':'B2','execution_id':'E1','requested_scope':['read','draft'],'reason':'Revised request'})
        self.call('decide_boundary', {'request_id':'B2','decision':'modified','modified_scope':['draft']})
        self.assertEqual(self.org.store.state()['Execution']['E1']['runtime_boundary'], ['draft'])
