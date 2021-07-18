from dataclasses import dataclass
from typing import Optional, List

from cloudrail.knowledge.context.azure.azure_resource import AzureResource
from cloudrail.knowledge.context.azure.constants.azure_resource_type import AzureResourceType


@dataclass
class AzureMonitorDiagnosticLogsRetentionPolicySettings:
    enabled: bool


@dataclass
class AzureMonitorDiagnosticLogsSettings:
    enabled: bool
    retention_policy: AzureMonitorDiagnosticLogsRetentionPolicySettings


class AzureMonitorDiagnosticSetting(AzureResource):
    """
        Attributes:
            name: The monitor diagnostic setting's name
            monitoring: The ID of the resource that is monitored
            logs_settings: The logs settings
    """

    def __init__(self, name: str, monitoring: str, logs_settings: Optional[AzureMonitorDiagnosticLogsSettings]):
        super().__init__(AzureResourceType.AZURERM_MONITOR_DIAGNOSTIC_SETTING)
        self.name: str = name
        self.monitoring: str = monitoring
        self.logs_settings: Optional[AzureMonitorDiagnosticLogsSettings] = logs_settings
        self.with_aliases(monitoring)

    def get_cloud_resource_url(self) -> Optional[str]:
        return f'https://portal.azure.com/#@{self.tenant_id}/resource/{self.monitoring}/diagnostics'

    @property
    def is_tagable(self) -> bool:
        return False

    def get_keys(self) -> List[str]:
        return [self._id]