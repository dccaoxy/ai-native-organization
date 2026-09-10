from organization.simulation import scenario, verify
from organization.store import Store
from tests.test_http import HTTPTests


class SimulationTests(HTTPTests):
    def test_complete_m01_over_real_http_interface(self):
        scenario(lambda **body:self.request('/api/commands', body))
        state = self.request('/api/state')['state']
        events = self.request('/api/events')['events']
        self.assertTrue(all(verify(state, events).values()))
        self.assertEqual(Store.replay(events), state)
        reopened = Store(self.httpd.organization.store.path)
        self.assertEqual(reopened.state(), state)

    def test_full_replay_is_idempotent(self):
        sender = lambda **body:self.request('/api/commands', body)
        first = scenario(sender)
        count = len(self.request('/api/events')['events'])
        second = scenario(sender)
        self.assertEqual(first, second)
        self.assertEqual(len(self.request('/api/events')['events']), count)
