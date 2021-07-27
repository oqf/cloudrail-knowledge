import unittest

from cloudrail.dev_tools.rule_test_utils import create_empty_entity
from cloudrail.knowledge.context.azure.azure_environment_context import AzureEnvironmentContext
from cloudrail.knowledge.context.azure.storage.azure_storage_account import AzureStorageAccount
from cloudrail.knowledge.rules.azure.non_context_aware.storage_account_secure_transfer import StorageAccountSecureTransfer
from cloudrail.knowledge.rules.base_rule import RuleResultType


class TestStorageAccountSecureTransfer(unittest.TestCase):
    def setUp(self):
        self.rule = StorageAccountSecureTransfer()

    def test_storage_account_secure_transfer_enabled(self):
        # Arrange
        storage_account: AzureStorageAccount = create_empty_entity(AzureStorageAccount)
        storage_account.enable_https_traffic_only = True
        storage_account.storage_name = 'storage_account'
        context = AzureEnvironmentContext(storage_accounts=[storage_account])
        # Act
        result = self.rule.run(context, {})
        # Assert
        self.assertEqual(RuleResultType.SUCCESS, result.status)

    def test_non_car_unused_network_security_group_pass_with_nic(self):
        # Arrange
        storage_account: AzureStorageAccount = create_empty_entity(AzureStorageAccount)
        storage_account.enable_https_traffic_only = False
        storage_account.storage_name = 'storage_account'
        context = AzureEnvironmentContext(storage_accounts=[storage_account])
        # Act
        result = self.rule.run(context, {})
        # Assert
        self.assertEqual(RuleResultType.FAILED, result.status)
        self.assertEqual(1, len(result.issues))
