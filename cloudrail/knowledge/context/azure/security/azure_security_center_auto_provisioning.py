from typing import List, Optional

from cloudrail.knowledge.context.azure.azure_resource import AzureResource
from cloudrail.knowledge.context.azure.constants.azure_resource_type import AzureResourceType


class AzureSecurityCenterAutoProvisioning(AzureResource):
    """
        Attributes:
            auto_provision_is_on: A flag indicating if auto provision is on
    """

    def __init__(self, auto_provision_is_on: bool):
        super().__init__(AzureResourceType.AZURERM_SECURITY_CENTER_AUTO_PROVISIONING)
        self.auto_provision_is_on: bool = auto_provision_is_on
        self.with_aliases(self.subscription_id)

    def get_cloud_resource_url(self) -> Optional[str]:
        pass
        # return f'https://portal.azure.com/#@{self.tenant_id}/resource/subscriptions/{self.subscription_id}/resourceGroups/' \
        #        f'{self.resource_group_name}/providers/Microsoft.Network/networkInterfaces/{self.name}/overview'

    @property
    def is_tagable(self) -> bool:
        return False

    def get_keys(self) -> List[str]:
        return [self.subscription_id]