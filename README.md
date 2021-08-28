# Fipper-python-sdk
A client library for python (SDK)

Fipper.io - a feature toggle (aka feature flags) software. More info https://fipper.io

## Install a synchronous version
> pip install fipper-python-sdk[sync]

## Install an asynchronous version (asyncio support)
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
    print(f'The `feature_flag` is available: {feature_flag.get_value()}')
else:
    print('The `feature_flag` is not available')
```

An AsyncClient example:
```python
import asyncio
from fipper_sdk import AsyncClient, FipperConfigNotFoundException


async def main():
    client = AsyncClient(
        environment=ENVIRONMENT,
        api_token=API_TOKEN,
        project_id=PROJECT_ID
    )

    try:
        config = await client.get_config()
    except FipperConfigNotFoundException:
        print('The config is not available or unpublished')
        exit(1)

    feature_flag = config.get_flag('my_feature_flag')  # `my_feature_flag` - it's a slug of a feature flag

    if feature_flag and feature_flag.available:
        print(f'The `feature_flag` is available: {feature_flag.get_value()}')
    else:
        print('The `feature_flag` is not available')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

More information and more client libraries: https://docs.fipper.io
