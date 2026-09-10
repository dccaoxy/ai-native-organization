from tests.test_work import WorkTests


class ReturnTests(WorkTests):
    def returned(self, number=1, command='submit'):
        return self.call(command, {'id':f'R{number}','execution_id':f'E{number}',
            'result':'Labelled simulation result','observed_terrain':'Fixture constraints',
            'major_execution_facts':'Public fixture actions','reflection':'Synthetic scenario, no real research conclusion'}, f'H{number}')

    def accepted(self, number=1, accepted=True, credible=True):
        self.call('review', {'id':f'V{number}','return_id':f'R{number}','credible':credible,'evidence':'Fixture evidence inspected'}, 'H2')
        self.call('accept', {'id':f'C{number}','return_id':f'R{number}','review_id':f'V{number}',
            'accepted':accepted,'rationale':'Assessed intended fixture use'}, 'H1')

    def test_parallel_returns_selection_preserves_losers(self):
        self.task()
        for i in range(1,4):
            self.execution(i)
            self.returned(i)
            self.accepted(i)
        self.call('select', {'id':'SEL1','task_id':'T1','return_id':'R2','rationale':'Best fit for fixture use'}, 'H3')
        state = self.org.store.state()
        self.assertEqual(len(state['Execution']), 3)
        self.assertEqual(len(state['Return']), 3)
        self.assertEqual(len(state['Review']), 3)
        self.assertEqual(len(state['Acceptance']), 3)
        self.assertEqual(state['Selection']['SEL1']['return_id'], 'R2')

    def test_failure_release_and_annotations_have_formal_returns(self):
        self.task()
        self.execution()
        self.request()
        self.returned(command='fail')
        self.assertEqual(self.org.store.state()['BoundaryRequest']['B1']['status'], 'cancelled')
        self.call('annotate_return', {'return_id':'R1','action':'correct','text':'Human fixture correction'})
        self.accepted(accepted=False)
        self.execution(2)
        self.returned(2, 'release')
        state = self.org.store.state()
        self.assertEqual(state['Execution']['E1']['status'], 'closed')
        self.assertEqual(state['Return']['R1']['outcome'], 'failure')
        self.assertEqual(state['Return']['R2']['outcome'], 'released')
        self.assertTrue(state['Return']['R1']['human_annotations'])
