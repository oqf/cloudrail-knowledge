from typing import Optional, List

from cloudrail.knowledge.context.azure.azure_resource import AzureResource
from cloudrail.knowledge.context.azure.constants.azure_resource_type import AzureResourceType


class AzureApplicationSecurityGroup(AzureResource):
    """
        Attributes:
            name: The ASG name
    """

    def __init__(self,
                 name: str):
        super().__init__(AzureResourceType.AZURERM_APPLICATION_SECURITY_GROUP)
        self.name: str = name

    def get_keys(self) -> List[str]:
        return [self.get_id()]

    def get_name(self) -> str:
        return self.name

    def get_cloud_resource_url(self) -> Optional[str]:
        pass

    def get_friendly_name(self) -> str:
        return self.get_name()

    @property
    def is_tagable(self) -> bool:
        return True
