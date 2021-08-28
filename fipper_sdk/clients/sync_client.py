import base64
import gzip
import json
from datetime import datetime

from fipper_sdk.clients.base import BaseClient
from fipper_sdk.exceptions import FipperException, FipperConfigNotFoundException
from fipper_sdk.manager import ConfigManager
from fipper_sdk.utils import SERVER_HOST

try:
    import requests
except ImportError:
    raise FipperException(message="The `requests` module hasn't installed. "
                                  "Try 'pip install fipper-python-sdk[sync]'")


class SyncClient(BaseClient):
    def get_config(self) -> ConfigManager:
        if actual_config := self._get_actual_config():
            return actual_config

        if self.previous_sync_date and self.config and self.etag:
            response = requests.head(f'{SERVER_HOST}/hash', params={
                'apiToken': self.api_token,
                'item': str(self.project_id),
                'eTag': self.etag
            })

            # The config is still the same
            #
            if response.status_code == 304:
                return self.config

        response = requests.get(f'{SERVER_HOST}/config', params={
            'apiToken': self.api_token,
            'item': str(self.project_id)
        })

        if response.status_code == 200:
            raw_data = response.json()
            config_env = raw_data['config'].get(self.environment)
            blob = json.loads(gzip.decompress(base64.b64decode(config_env)))\
                if config_env else dict()

            self.config = ConfigManager(config_data=blob)
            self.etag = raw_data['eTag']
            self.previous_sync_date = datetime.utcnow()
        elif not self.config:
            raise FipperConfigNotFoundException()
        return self.config
