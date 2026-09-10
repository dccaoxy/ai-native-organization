"""Persist one actual cloud observation per candidate/state, without poll noise."""
import os
from pathlib import Path
import subprocess
from autodev.runtime import Harness, digest, read, write


def main():
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REF') != 'refs/heads/main' or os.environ.get('GITHUB_EVENT_NAME') == 'pull_request':
        raise RuntimeError('Cloud receipt requires the trusted default-branch workflow')
    h = Harness(Path.cwd())
    stages = {sid:{'status':s['status'],'tag':s.get('tag'),'source_digest':s.get('source_digest')}
              for sid,s in h.state['stages'].items()}
    fingerprint = digest({'source':h.manifest(h.plan['stages'][-1]),'stages':stages})
    path = h.home / 'CLOUD_RECEIPT.json'
    if path.exists() and read(path).get('fingerprint') == fingerprint:
        print('Unchanged verified candidate/state; retain existing cloud receipt')
        return
    run_id = os.environ['GITHUB_RUN_ID']
    repo = os.environ['GITHUB_REPOSITORY']
    write(path, {'kind':'actual GitHub Actions runtime observation, not new milestone acceptance',
                 'fingerprint':fingerprint,'run_id':run_id,
                 'url':f'https://github.com/{repo}/actions/runs/{run_id}',
                 'input_commit':os.environ['GITHUB_SHA'],'stages':stages,
                 'runner':'GitHub-hosted Linux','model_builder_configured':False,
                 'writeback':'This receipt is committed locally here; remote delivery must be verified from origin.'})
    h.git('add','--',str(path.relative_to(h.root)))
    h.git('commit','-m','chore(autodev): persist verified cloud runner receipt')
    print('Cloud receipt committed; workflow must push and verify remote delivery')


if __name__ == '__main__': main()
