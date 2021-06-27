from typing import List, Optional

from cloudrail.knowledge.context.gcp.constants.gcp_resource_type import GcpResourceType
from cloudrail.knowledge.context.gcp.gcp_resource import GcpResource


class GcpSqlDatabaseInstance(GcpResource):
    """
        Attributes:
            name: The name of this SQL database instance
            require_ssl: An indication on if this instance requires SSL
    """

    def __init__(self, name: str, require_ssl: bool):
        super().__init__(GcpResourceType.GOOGLE_SQL_DATABASE_INSTANCE)
        self.name: str = name
        self.require_ssl: bool = require_ssl

    def get_keys(self) -> List[str]:
        return [self.name, self.project_id]

    @property
    def is_tagable(self) -> bool:
        return False

    def get_id(self) -> str:
        return self.name

    def get_cloud_resource_url(self) -> Optional[str]:
        return f'https://console.cloud.google.com/sql/instances/{self.name}/'