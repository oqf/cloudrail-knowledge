from typing import Optional, List

from cloudrail.knowledge.context.azure.azure_resource import AzureResource
from cloudrail.knowledge.context.azure.constants.azure_resource_type import AzureResourceType
from cloudrail.knowledge.context.azure.keyvault.azure_monitor_diagnostic_setting import AzureMonitorDiagnosticSetting


class AzureKeyVault(AzureResource):
    """
        Attributes:
            name: The KeyVault name
            monitor_diagnostic_settings: The monitoring settings of this KeyVault
    """

    def __init__(self, name: str):
        super().__init__(AzureResourceType.AZURERM_KEY_VAULT)
        self.name: str = name
        self.monitor_diagnostic_settings: AzureMonitorDiagnosticSetting = None

    def get_cloud_resource_url(self) -> Optional[str]:
        return f'https://portal.azure.com/#@{self.tenant_id}/resource/subscriptions/{self.subscription_id}/resourceGroups/' \
               f'{self.resource_group_name}/providers/Microsoft.KeyVault/vaults/{self.name}/overview'

    @property
    def is_tagable(self) -> bool:
        return True

    def get_keys(self) -> List[str]:
        return [self._id]

    def exclude_from_invalidation(self):
        return [self.monitor_diagnostic_settings]

    def custom_invalidation(self) -> List[str]:
        if self.monitor_diagnostic_settings and self.monitor_diagnostic_settings.is_invalidated:
            return ["The KeyVault's monitor diagnostic setting is invalid"]
        return []