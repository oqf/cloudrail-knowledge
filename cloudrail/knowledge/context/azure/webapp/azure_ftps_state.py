from enum import Enum


class FtpsState(Enum):
    ALL_ALLOWED = 'AllAllowed'
    FTPS_ONLY = 'FtpsOnly'
    DISABLED = 'Disabled'
