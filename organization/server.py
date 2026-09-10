"""Loopback-only simulation HTTP/Agent interface. Real mode is gated elsewhere."""
import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import secrets
from urllib.parse import urlsplit

from organization.core import Organization, require
from organization.store import DomainError


def server(path, port=0):
    org = Organization(path)
    csrf = secrets.token_urlsafe(32)
    web = Path(__file__).parent / 'web'

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args): pass

        def allowed_host(self):
            return self.headers.get('Host') in (f'127.0.0.1:{self.server.server_port}', f'localhost:{self.server.server_port}')

        def respond(self, status, body, content_type='application/json; charset=utf-8'):
            payload = json.dumps(body, ensure_ascii=False).encode() if content_type.startswith('application/json') else body.encode()
            self.send_response(status)
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Length', str(len(payload)))
            self.send_header('Cache-Control', 'no-store')
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; frame-ancestors 'none'")
            self.end_headers()
            self.wfile.write(payload)

        def do_GET(self):
            if not self.allowed_host(): return self.respond(403, {'error':'Untrusted Host'})
            path = urlsplit(self.path).path
            if path == '/':
                return self.respond(200, (web / 'index.html').read_text(encoding='utf-8').replace('__CSRF__', csrf), 'text/html; charset=utf-8')
            if path in ('/app.js','/style.css'):
                return self.respond(200, (web / path[1:]).read_text(encoding='utf-8'), 'text/javascript' if path.endswith('.js') else 'text/css')
            if self.headers.get('X-Simulation-Token') != csrf: return self.respond(403, {'error':'Simulation session token required'})
            try:
                if path == '/api/state': return self.respond(200, {'simulation':True,'state':org.store.state()})
                if path == '/api/events': return self.respond(200, {'simulation':True,'events':org.store.events()})
                if path == '/api/task-wall': return self.respond(200, {'simulation':True,'tasks':[t for t in org.store.state().get('Task', {}).values() if t['status'] == 'published']})
                return self.respond(404, {'error':'Not found'})
            except DomainError as exc: return self.respond(exc.status, {'error':str(exc)})

        def do_POST(self):
            if not self.allowed_host(): return self.respond(403, {'error':'Untrusted Host'})
            origin = self.headers.get('Origin')
            if origin and origin != 'http://' + self.headers.get('Host', ''):
                return self.respond(403, {'error':'Cross-origin mutation denied'})
            if self.headers.get('X-Simulation-Token') != csrf: return self.respond(403, {'error':'Simulation session token required'})
            if self.path != '/api/commands': return self.respond(404, {'error':'Not found'})
            try:
                length = int(self.headers.get('Content-Length','0'))
                if not 0 < length <= 65536: return self.respond(413, {'error':'Command size must be 1..65536 bytes'})
                body = json.loads(self.rfile.read(length))
                require(body, ['actor','command','data','idempotency_key'])
                result = org.execute(**body)
                return self.respond(200, {'simulation':True, **result})
            except DomainError as exc: return self.respond(exc.status, {'error':str(exc)})
            except (ValueError, TypeError, KeyError) as exc: return self.respond(400, {'error':'Invalid command shape or value'})

    httpd = ThreadingHTTPServer(('127.0.0.1', port), Handler)
    httpd.organization = org
    return httpd


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--db', default='.autodev/organization.sqlite3')
    parser.add_argument('--port', type=int, default=8765)
    args = parser.parse_args()
    httpd = server(args.db, args.port)
    print(f'M01 simulation workspace: http://127.0.0.1:{httpd.server_port}', flush=True)
    try: httpd.serve_forever()
    except KeyboardInterrupt: pass
    finally: httpd.server_close()


if __name__ == '__main__': main()
