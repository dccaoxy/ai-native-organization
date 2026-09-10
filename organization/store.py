"""Transactional append-only event store; command receipt and facts commit together."""
import copy
import hashlib
import json
from pathlib import Path
import sqlite3
import time
import uuid
from contextlib import contextmanager

from autodev.runtime import canonical, digest
from organization.contracts import validate


class DomainError(ValueError):
    def __init__(self, message, status=400):
        super().__init__(message)
        self.status = status


class Store:
    def __init__(self, path, clock=time.time):
        self.path = str(path)
        self.clock = clock
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as db:
            db.executescript('''
                CREATE TABLE IF NOT EXISTS events (
                    sequence INTEGER PRIMARY KEY, envelope TEXT NOT NULL,
                    previous_hash TEXT NOT NULL, hash TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS receipts (
                    key TEXT PRIMARY KEY, request_hash TEXT NOT NULL, response TEXT NOT NULL);
            ''')

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.path, timeout=15)
        db.execute('PRAGMA journal_mode=WAL')
        db.execute('PRAGMA synchronous=FULL')
        try:
            with db:
                yield db
        finally:
            db.close()

    def _events(self, db):
        result, previous = [], 'genesis'
        for seq, raw, prior, sha in db.execute('SELECT sequence,envelope,previous_hash,hash FROM events ORDER BY sequence'):
            event = json.loads(raw)
            if seq != len(result) + 1 or event['sequence'] != seq or prior != previous or digest([prior, event]) != sha:
                raise DomainError('Event integrity failure', 409)
            validate('OrganizationalEvent', event)
            result.append(event)
            previous = sha
        return result, previous

    @staticmethod
    def replay(events):
        state = {}
        for event in events:
            for kind, objects in event['changes'].items():
                state.setdefault(kind, {}).update(copy.deepcopy(objects))
        return state

    def events(self):
        with self.connect() as db:
            return self._events(db)[0]

    def state(self):
        return self.replay(self.events())

    def transact(self, actor, command, data, key, handler):
        if not isinstance(key, str) or not key.strip() or len(key) > 200:
            raise DomainError('A bounded nonempty idempotency key is required')
        request_hash = digest({'actor':actor,'command':command,'data':data})
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            receipt = db.execute('SELECT request_hash,response FROM receipts WHERE key=?', (key,)).fetchone()
            if receipt:
                if receipt[0] != request_hash:
                    raise DomainError('Idempotency key reused for a different command', 409)
                return json.loads(receipt[1])
            events, previous = self._events(db)
            state = self.replay(events)
            emitted = handler(state)
            if not emitted and command != 'sweep':
                raise DomainError('A mutation must produce formal evidence')
            created = []
            for change in emitted:
                event = {'id':uuid.uuid4().hex,'sequence':len(events) + len(created) + 1,
                         'type':change['type'],'actor':actor,'authority_source':change['authority'],
                         'accountable_owner':change.get('owner','not-applicable'),
                         'correlation_id':change.get('correlation', key),'causation_id':key,
                         'idempotency_key':key,'occurred_at':self.clock(),'simulation':True,
                         'changes':change['changes']}
                validate('OrganizationalEvent', event)
                sha = digest([previous,event])
                db.execute('INSERT INTO events VALUES (?,?,?,?)', (event['sequence'],canonical(event),previous,sha))
                created.append(event)
                previous = sha
            response = {'events':created,'state':self.replay(events + created)}
            db.execute('INSERT INTO receipts VALUES (?,?,?)', (key,request_hash,canonical(response)))
            return response
