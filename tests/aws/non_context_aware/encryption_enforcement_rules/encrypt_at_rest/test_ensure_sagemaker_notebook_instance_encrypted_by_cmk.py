
# import unittest
#
# from cloudrail.knowledge.context.environment_context import EnvironmentContext
# from cloudrail.knowledge.rules.base_rule import RuleResultType
# from cloudrail.dev_tools.rule_test_utils import create_empty_entity
#
#
# class TestEnsureSageMakerNotebookInstanceEncryptedAtRestByCMKRule(unittest.TestCase):
#     def setUp(self):
#         self.rule = EnsureSageMakerNotebookInstanceEncryptedAtRestByCMKRule()
#
#     def test_not_car_sagemaker_notebook_instances_encrypt_artifacts_at_rest_with_customer_managed_CMK_creating_fail(self):
#         # Arrange
#         context = EnvironmentContext()
#         # Act
#         result = self.rule.run(context, {})
#         # Assert
#         self.assertEqual(RuleResultType.FAILED, result.status)
#         self.assertEqual(1, len(result.issues))
#
#     def test_not_car_sagemaker_notebook_instances_encrypt_artifacts_at_rest_with_customer_managed_CMK_creating_pass(self):
#         # Arrange
#         context = EnvironmentContext()
#         # Act
#         result = self.rule.run(context, {})
#         # Assert
#         self.assertEqual(RuleResultType.SUCCESS, result.status)
#         self.assertEqual(0, len(result.issues))
