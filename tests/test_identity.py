from pathlib import Path
import tempfile
import unittest
from organization.core import Organization
from organization.identity import DELEGABLE
from tests.test_core import CoreTests


class IdentityTests(CoreTests):
    def test_binding_replacement_preserves_human_accountability(self):
        self.task()
        self.execution()
        self.call('bind_agent', {'hau_id':'U1','agent_id':'A4','permissions':['claim','ack']})
        state = self.org.store.state()
        self.assertFalse(state['RepresentativeAgent']['A1']['active'])
        self.assertTrue(state['RepresentativeAgent']['A4']['active'])
        self.assertEqual(state['Execution']['E1']['accountable_owner'], 'H1')

    def test_agent_offline_makes_execution_visible(self):
        self.task()
        self.execution()
        self.call('agent_status', {'agent_id':'A1','runtime_status':'offline'}, 'A1')
        self.assertEqual(self.org.store.state()['Execution']['E1']['status'], 'interrupted')
        self.assertEqual(self.org.store.events()[-1]['type'], 'ExecutionInterrupted')

    def test_ack_timeout_survives_worker_restart(self):
        self.task()
        self.call('claim', {'id':'E1','task_id':'T1','hau_id':'U1'})
        when = self.org.store.state()['Execution']['E1']['last_seen']
        reopened = Organization(self.org.store.path, clock=lambda:when + 301)
        reopened.execute('SIMULATOR','sweep',{},'clock-sweep')
        self.assertEqual(reopened.store.state()['Execution']['E1']['status'], 'interrupted')
        self.assertEqual(reopened.execute('SIMULATOR','sweep',{},'no-op-sweep')['events'], [])

    def test_bootstrap_real_command_path(self):
        self.call('register_human', {'id':'H4','display_name':'Simulation participant 4'}, 'SIMULATOR')
        self.call('bind_agent', {'hau_id':'U4','agent_id':'A4','permissions':sorted(DELEGABLE)}, 'H4')
        self.assertEqual(self.org.store.state()['HAU']['U4']['human_id'], 'H4')
