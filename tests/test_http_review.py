from urllib.error import HTTPError
from tests.test_http import HTTPTests


class HTTPReview(HTTPTests):
    def test_unauthenticated_and_cross_origin_commands_rejected(self):
        body = {'actor':'SIMULATOR','command':'register_human','data':{'id':'H1','display_name':'x'},'idempotency_key':'x'}
        for headers in ({'X-Simulation-Token':'wrong'},{'Origin':'https://unrelated.invalid'},{'Host':'attacker.invalid'}):
            with self.assertRaises(HTTPError) as caught: self.request('/api/commands', body, headers)
            self.assertEqual(caught.exception.code, 403)
        self.assertEqual(self.request('/api/events')['events'], [])

    def test_malformed_and_path_traversal_do_not_mutate(self):
        for body in ([], {'actor':'H1'}, {'actor':'SIMULATOR','command':'register_human','data':{'id':'H1','display_name':'x','private_thought':'x'},'idempotency_key':'x'}):
            with self.assertRaises(HTTPError) as caught: self.request('/api/commands', body)
            self.assertEqual(caught.exception.code, 400)
        with self.assertRaises(HTTPError) as caught: self.request('/../../AGENTS.md')
        self.assertEqual(caught.exception.code, 404)
        self.assertEqual(self.request('/api/events')['events'], [])
