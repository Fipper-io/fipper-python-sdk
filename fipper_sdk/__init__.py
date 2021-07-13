from fipper_sdk.manager import ConfigManager
from fipper_sdk.utils import Rate


modules = [
    'ConfigManager',
    'Rate'
]

try:
    import requests
except ImportError:
    pass
else:
    from fipper_sdk.client.sync import *
    modules.append('SyncClient')


__all__ = modules
