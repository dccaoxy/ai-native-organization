from urllib.error import HTTPError
from organization.simulation import scenario, verify
from tests.test_http import HTTPTests


class SimulationReview(HTTPTests):
    def test_closed_task_keeps_evidence_and_rejects_new_claim(self):
        scenario(lambda **body:self.request('/api/commands', body))
        prior = self.request('/api/events')['events']
        with self.assertRaises(HTTPError) as caught:
            self.request('/api/commands', {'actor':'H1','command':'claim','data':{'id':'E9','task_id':'T1','hau_id':'U1'},'idempotency_key':'late-claim'})
        self.assertEqual(caught.exception.code, 409)
        self.assertEqual(self.request('/api/events')['events'], prior)
        state = self.request('/api/state')['state']
        self.assertTrue(all(verify(state, prior).values()))
        self.assertNotIn('private_thought', str(prior))

    def test_authority_chain_survives_event_replay(self):
        scenario(lambda **body:self.request('/api/commands', body))
        events = self.request('/api/events')['events']
        for event in events:
            self.assertTrue(event['authority_source'])
            if event['type'] in ('BoundaryApproved','ResultReviewed','ResultAccepted','ResultSelected'):
                self.assertTrue(event['actor'].startswith('H'))
        self.assertEqual([e['sequence'] for e in events], list(range(1,len(events)+1)))
