from fipper_sdk.manager import ConfigManager


modules = [
    'ConfigManager'
]

try:
    import requests
except ImportError:
    pass
else:
    from fipper_sdk.fetcher.basic import *
    modules.append('BasicSync')


__all__ = modules
