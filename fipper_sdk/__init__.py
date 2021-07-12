from fipper_sdk import Rate
from fipper_sdk.manager import ConfigManager


modules = [
    'ConfigManager',
    'Rate'
]

try:
    import requests
except ImportError:
    pass
else:
    from fipper_sdk.fetcher.basic import *
    modules.append('BasicSync')


__all__ = modules
