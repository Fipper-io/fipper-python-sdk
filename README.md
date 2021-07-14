# Fipper-python-sdk
A client library for python (SDK)

Fipper.io - a feature toggle (aka feature flags) software. More info https://fipper.io

## Installing a synchronous version
> pip install fipper-python-sdk[sync]

## Installing an asynchronous version (asyncio support)
> pip install fipper-python-sdk[async]

## Example
Here are some credentials:
```python
ENVIRONMENT = 'production' 
API_TOKEN = '* place your token here *'
PROJECT_ID = 12345
```

A code snippet for a sync version:
```python
from fipper_sdk import SyncClient, FipperConfigNotFoundException


client = SyncClient(
    environment=ENVIRONMENT,
    api_token=API_TOKEN,
    project_id=PROJECT_ID
)

try:
    config = client.get_config()
except FipperConfigNotFoundException:
    print('The config is not available or unpublished')
    exit(1)

feature_flag = config.get_flag('my_feature_flag')  # `my_feature_flag` - it's a slug of a feature flag

if feature_flag and feature_flag.available:
    print('The `feature_flag` is available')
else:
    print('The `feature_flag` is not available')
```

More information and more clients: https://docs.fipper.io
