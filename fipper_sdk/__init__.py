from fipper_sdk.exceptions import FipperException, FipperConfigNotFoundException
from fipper_sdk.manager import ConfigManager
from fipper_sdk.utils import Rate


modules = [
    'ConfigManager',
    'Rate',
    'FipperException',
    'FipperConfigNotFoundException'
]

try:
    import requests
except ImportError:
    pass
else:
    from fipper_sdk.clients.sync_client import *
    modules.append('SyncClient')


try:
    import aiohttp
except ImportError:
    pass
else:
    from fipper_sdk.clients.async_client import *
    modules.append('AsyncClient')


__all__ = modules
