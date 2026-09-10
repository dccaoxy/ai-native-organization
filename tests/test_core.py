from pathlib import Path
import tempfile
import unittest
from organization.core import Organization


class CoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.org = Organization(Path(self.tmp.name) / 'org.sqlite3')
        # Explicit fixtures isolate core testing from the later Identity stage.
        changes = {'Human':{},'HAU':{},'RepresentativeAgent':{}}
        for i in range(1,4):
            h,a,u = f'H{i}',f'A{i}',f'U{i}'
            changes['Human'][h] = {'id':h,'display_name':'Simulation ' + h,'kind':'human'}
            changes['HAU'][u] = {'id':u,'human_id':h,'agent_id':a}
            changes['RepresentativeAgent'][a] = {'id':a,'human_id':h,'hau_id':u,'active':True,'permissions':['claim','ack','progress','blocked','escalate','resume','request_boundary','submit','fail','release'],'runtime_status':'online'}
        self.org.store.transact('SIMULATOR','fixture',{},'seed',lambda s:[{'type':'FixtureSeed','authority':'test fixture','changes':changes}])
        self.counter = 0

    def tearDown(self): self.tmp.cleanup()

    def call(self, command, data, actor='H1'):
        self.counter += 1
        return self.org.execute(actor, command, data, str(self.counter))

    def task(self):
        self.call('activate_goal', {'id':'G1','desired_change':'Simulation outcome','success_criteria':'Explicit fixture criterion','boundary':['read','draft'],'goal_authority':'H1'})
        self.call('create_task', {'id':'T1','primary_goal':'G1','expected_output':'Fixture result','acceptance_criteria':'Evidence matches fixture criterion','boundary':['read'],'execution_mode':'parallel','review_authority':'H2','acceptance_authority':'H1','selection_authority':'H3'})
        self.call('publish', {'task_id':'T1'})

    def execution(self, number=1):
        self.call('claim', {'id':f'E{number}','task_id':'T1','hau_id':f'U{number}'}, f'H{number}')
        self.call('ack', {'execution_id':f'E{number}'}, f'H{number}')

    def test_three_claims_are_three_attempts(self):
        self.task()
        for i in range(1,4): self.execution(i)
        state = self.org.store.state()
        self.assertEqual(len(state['Task']), 1)
        self.assertEqual(len(state['Execution']), 3)
        self.assertEqual({e['accountable_owner'] for e in state['Execution'].values()}, {'H1','H2','H3'})
        self.assertEqual(state['Task']['T1']['status'], 'published')
