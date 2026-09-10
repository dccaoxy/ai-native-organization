"""Negative expectations independently transcribed from TASK/WORK/AGENT L2."""
import unittest
from organization.contracts import CONTRACT, validate


class ContractReview(unittest.TestCase):
    def test_task_cannot_swallow_attempt_or_accountability(self):
        task, execution = CONTRACT['objects']['Task'], CONTRACT['objects']['Execution']
        self.assertNotIn('accountable_owner', task)
        self.assertNotIn('hau_id', task)
        self.assertEqual(execution['accountable_owner']['type'], 'string')
        self.assertIn('task_id', execution)

    def test_private_thought_and_ambiguous_human_rejected(self):
        for body in ({'id':'H1','display_name':'x','kind':'agent'},
                     {'id':'H1','display_name':'x','kind':'human','private_thought':'secret'},
                     {'id':['H1','H2'],'display_name':'x','kind':'human'}):
            with self.assertRaises(ValueError): validate('Human', body)
        for name in CONTRACT['objects']:
            self.assertFalse({'private_thought','drafts','chain_of_thought'} & CONTRACT['objects'][name].keys())

    def test_decisions_and_returns_cannot_be_collapsed(self):
        self.assertNotEqual(CONTRACT['objects']['Review'], CONTRACT['objects']['Acceptance'])
        self.assertNotEqual(CONTRACT['objects']['Acceptance'], CONTRACT['objects']['Selection'])
        for key in ('result','observed_terrain','major_execution_facts','reflection'):
            self.assertIn(key, CONTRACT['objects']['Return'])
        self.assertIn('Human', CONTRACT['authority_matrix']['decide_boundary'])
        self.assertIn('Human', CONTRACT['authority_matrix']['activate_goal'])
