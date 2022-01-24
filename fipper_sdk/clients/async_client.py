import base64
import gzip
import json
from datetime import datetime

from fipper_sdk.clients.base import BaseClient
from fipper_sdk.exceptions import FipperException, FipperConfigNotFoundException
from fipper_sdk.manager import ConfigManager
from fipper_sdk.utils import SERVER_HOST

try:
    import aiohttp
except ImportError:
    raise FipperException(message="The `aiohttp` module hasn't installed. "
                                  "Try 'pip install fipper-python-sdk[async]'")


class AsyncClient(BaseClient):
    async def get_config(self) -> ConfigManager:
        if actual_config := self._get_actual_config():
            return actual_config

        if self.previous_sync_date and self.config and self.etag:
            async with aiohttp.ClientSession() as session:
                async with session.head(
                        f'{SERVER_HOST}/hash',
                        params={
                            'apiToken': self.api_token,
                            'item': str(self.project_id),
                            'eTag': self.etag
                        }
                ) as response:
                    # The config is still the same
                    #
                    if response.status == 304:
                        return self.config

        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'{SERVER_HOST}/config',
                    params={
                        'apiToken': self.api_token,
                        'item': str(self.project_id)
                    }
            ) as response:
                if response.status == 200:
                    raw_data = await response.json(content_type=None)
                    config_env = raw_data['config'].get(self.environment)
                    blob = json.loads(gzip.decompress(base64.b64decode(config_env)))\
                        if config_env else dict()

                    self.config = ConfigManager(config_data=blob)
                    self.etag = raw_data['eTag']
                    self.previous_sync_date = datetime.utcnow()
                elif not self.config:
                    raise FipperConfigNotFoundException()
        return self.config
