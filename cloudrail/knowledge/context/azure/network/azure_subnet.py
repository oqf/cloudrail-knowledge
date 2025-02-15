from typing import List, Optional

from cloudrail.knowledge.context.azure.azure_resource import AzureResource
from cloudrail.knowledge.context.azure.constants.azure_resource_type import AzureResourceType
from cloudrail.knowledge.context.azure.network.azure_network_security_group import AzureNetworkSecurityGroup


class AzureSubnet(AzureResource):
    """
        Attributes:
            name: The name of this subnet
            network_security_group_id: The id of the network security group that's attached to this subnet.
            network_security_group: The actual security group that's attached to this subnet.
    """

    def __init__(self, network_security_group_id: Optional[str], name: str):
        super().__init__(AzureResourceType.AZURERM_NETWORK_SECURITY_GROUP)
        self.network_security_group_id: Optional[str] = network_security_group_id
        self.name: str = name

        self.network_security_group: Optional[AzureNetworkSecurityGroup] = None

    def get_cloud_resource_url(self) -> Optional[str]:
        pass  # Requires VNET

    @property
    def is_tagable(self) -> bool:
        return False

    def get_keys(self) -> List[str]:
        return [self.get_id()]
