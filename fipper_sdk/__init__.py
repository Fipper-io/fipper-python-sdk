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
    from fipper_sdk.client.basic import *
    modules.append('BasicSync')


__all__ = modules
