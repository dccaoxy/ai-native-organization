from organization.store import DomainError
from tests.test_identity import IdentityTests


class IdentityReview(IdentityTests):
    def test_no_agent_can_delegate_human_authority(self):
        with self.assertRaises(DomainError):
            self.call('bind_agent', {'hau_id':'U1','agent_id':'A9','permissions':['claim']}, 'A1')
        with self.assertRaises(DomainError):
            self.call('bind_agent', {'hau_id':'U1','agent_id':'A9','permissions':['decide_boundary']})

    def test_replaced_agent_cannot_act_and_cannot_reassign_hau(self):
        self.task()
        self.call('bind_agent', {'hau_id':'U1','agent_id':'A9','permissions':['claim']})
        with self.assertRaises(DomainError): self.call('claim', {'id':'E1','task_id':'T1','hau_id':'U1'}, 'A1')
        with self.assertRaises(DomainError): self.call('bind_agent', {'hau_id':'U1','agent_id':'A8','permissions':[]}, 'H2')
        with self.assertRaises(DomainError): self.call('bind_agent', {'hau_id':'U1','agent_id':'H2','permissions':[]})

    def test_permission_is_not_inferred_from_capability(self):
        self.task()
        self.call('bind_agent', {'hau_id':'U1','agent_id':'A9','permissions':[]})
        with self.assertRaises(DomainError): self.call('claim', {'id':'E1','task_id':'T1','hau_id':'U1'}, 'A9')
