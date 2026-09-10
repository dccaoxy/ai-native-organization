import json
from pathlib import Path
import re
import tempfile
import threading
import unittest
from urllib.request import Request, urlopen
from organization.server import server


class HTTPTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.httpd = server(Path(self.tmp.name) / 'http.sqlite3')
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.thread.start()
        self.url = f'http://127.0.0.1:{self.httpd.server_port}'
        with urlopen(self.url) as response: self.html = response.read().decode()
        self.token = re.search(r'name="simulation-token" content="([^"]+)"', self.html).group(1)

    def tearDown(self):
        self.httpd.shutdown()
        self.httpd.server_close()
        self.thread.join()
        self.tmp.cleanup()

    def request(self, path, body=None, headers=None):
        all_headers = {'X-Simulation-Token':self.token,'Content-Type':'application/json', **(headers or {})}
        req = Request(self.url + path, json.dumps(body).encode() if body is not None else None, headers=all_headers)
        with urlopen(req) as response: return json.loads(response.read())

    def test_http_command_query_persistence_and_ui(self):
        body = {'actor':'SIMULATOR','command':'register_human','data':{'id':'H1','display_name':'HTTP simulation fixture'},'idempotency_key':'h1'}
        first = self.request('/api/commands', body)
        self.assertEqual(first, self.request('/api/commands', body))
        self.assertEqual(self.request('/api/state')['state']['Human']['H1']['id'], 'H1')
        self.assertEqual(len(self.request('/api/events')['events']), 1)
        self.assertIn('Free Work Space', self.html)
        self.assertIn('仅合成场景', self.html)
