import unittest

from cloudrail.dev_tools.rule_test_utils import create_empty_entity
from cloudrail.knowledge.context.aws.workspaces.workspaces import Workspace
from cloudrail.knowledge.context.environment_context import EnvironmentContext
from cloudrail.knowledge.context.terraform_state import TerraformState
from cloudrail.knowledge.rules.aws.non_context_aware.encryption_enforcement_rules.\
    encrypt_at_rest.ensure_workspace_root_volume_encrypted_at_rest_rule import EnsureWorkspaceRootVolumeEncryptedAtRestRule
from cloudrail.knowledge.rules.base_rule import RuleResultType


class TestEnsureWorkspaceRootVolumeEncryptedAtRestRule(unittest.TestCase):
    def setUp(self):
        self.rule = EnsureWorkspaceRootVolumeEncryptedAtRestRule()

    def test_non_car_workspace_root_volume_encrypt_at_rest_creating_fail(self):
        # Arrange
        workspace: Workspace = create_empty_entity(Workspace)
        terraform_state = create_empty_entity(TerraformState)
        workspace.terraform_state = terraform_state
        workspace.terraform_state.is_new = True
        workspace.root_encryption_enabled = False
        context = EnvironmentContext(workspaces=[workspace])
        # Act
        result = self.rule.run(context, {})
        # Assert
        self.assertEqual(RuleResultType.FAILED, result.status)
        self.assertEqual(1, len(result.issues))

    def test_non_car_workspace_root_volume_encrypt_at_rest_creating_pass(self):
        # Arrange
        workspace: Workspace = create_empty_entity(Workspace)
        terraform_state = create_empty_entity(TerraformState)
        workspace.terraform_state = terraform_state
        workspace.terraform_state.is_new = True
        workspace.root_encryption_enabled = True
        context = EnvironmentContext(workspaces=[workspace])
        # Act
        result = self.rule.run(context, {})
        # Assert
        self.assertEqual(RuleResultType.SUCCESS, result.status)
        self.assertEqual(0, len(result.issues))

    def test_non_car_workspace_root_volume_encrypt_at_rest_creating__not_new__pass(self):
        # Arrange
        workspace: Workspace = create_empty_entity(Workspace)
        terraform_state = create_empty_entity(TerraformState)
        workspace.terraform_state = terraform_state
        workspace.terraform_state.is_new = False
        workspace.root_encryption_enabled = False
        context = EnvironmentContext(workspaces=[workspace])
        # Act
        result = self.rule.run(context, {})
        # Assert
        self.assertEqual(RuleResultType.SUCCESS, result.status)
        self.assertEqual(0, len(result.issues))