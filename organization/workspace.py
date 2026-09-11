"""One stable local entry; preserves prior labs and never merges their data."""
import argparse,json,os,secrets,sqlite3
from contextlib import closing
from pathlib import Path
from organization.agent_gateway import server


def prepare(root,seed=None):
    root=Path(root);root.mkdir(parents=True,exist_ok=True)
    db=root/'workspace.sqlite3';key=root/'workspace.key'
    if seed:
        if db.exists():raise ValueError('Unified workspace already exists; seed import refused')
        source=Path(seed).resolve()
        if not source.is_file():raise ValueError('Seed database does not exist')
        # Consistent SQLite backup includes committed WAL; source opened read-only.
        try:
            with closing(sqlite3.connect(source.as_uri()+'?mode=ro',uri=True)) as src:
                if not src.execute("SELECT 1 FROM sqlite_master WHERE name='events'").fetchone():raise ValueError('Not an organization event database')
                with closing(sqlite3.connect(db)) as dst:src.backup(dst)
        except Exception:
            # Only this freshly created destination is removed after failed import.
            if db.exists():db.unlink()
            raise
    if not key.exists():
        fd=os.open(key,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
        with os.fdopen(fd,'w') as stream:stream.write(secrets.token_urlsafe(32))
    return db,key


def main():
    p=argparse.ArgumentParser();p.add_argument('--directory',default='.autodev/unified');p.add_argument('--port',type=int,default=8877);p.add_argument('--seed-from');a=p.parse_args()
    db,key=prepare(a.directory,a.seed_from)
    http=server(db,key.read_text().strip(),a.port)
    info={'url':f'http://127.0.0.1:{http.server_port}','database':str(db.resolve()),'key_file':str(key.resolve()),'mode':'local synthetic workspace; no cloud persistence claim'}
    (Path(a.directory)/'workspace.json').write_text(json.dumps(info,indent=2),encoding='utf-8')
    print('Unified workspace: '+info['url']+'; local key file: '+str(key),flush=True)
    try:http.serve_forever()
    except KeyboardInterrupt:pass
    finally:http.server_close()

if __name__=='__main__':main()
