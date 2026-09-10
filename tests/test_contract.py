import unittest
from organization.contracts import CONTRACT, validate


class ContractTests(unittest.TestCase):
    def test_all_core_objects_have_concrete_fields(self):
        for name in ('Human','HAU','RepresentativeAgent','Goal','Task','Execution','BoundaryRequest','Return','Review','Acceptance','Selection','OrganizationalEvent'):
            self.assertIn('id', CONTRACT['objects'][name])
        self.assertEqual(validate('Human', {'id':'H1','display_name':'Fixture Human','kind':'human'})['id'], 'H1')

    def test_event_envelope_and_state_transitions(self):
        event = CONTRACT['objects']['OrganizationalEvent']
        for field in ('actor','authority_source','accountable_owner','idempotency_key','correlation_id','causation_id','occurred_at','changes','simulation'):
            self.assertIn(field, event)
        ex = CONTRACT['state_machines']['Execution']
        self.assertEqual(ex['ack'], {'from':['claimed'], 'to':'running'})
        self.assertNotIn('running', ex['close']['from'])
        self.assertIn('interrupt', ex)

    def test_inputs_and_parameters_are_explicit(self):
        self.assertIn('decide_boundary', CONTRACT['authority_matrix'])
        self.assertIn('idempotency_key', CONTRACT['interface']['command'])
        self.assertEqual(CONTRACT['parameters']['ack_timeout_seconds']['classification'], 'Tunable')
        self.assertGreaterEqual(len(CONTRACT['pages']), 6)
