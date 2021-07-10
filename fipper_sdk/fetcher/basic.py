import gzip
import json
from datetime import datetime, timedelta
from typing import Optional

from fipper_sdk.exceptions import FipperException
from fipper_sdk.utils import Rate
from fipper_sdk.manager import ConfigManager
from fipper_sdk.utils import SERVER_HOST

try:
    import requests
except ImportError:
    raise FipperException(message="The `requests` module hasn't installed. "
                                  "Try 'pip install fipper-python-sdk[sync]'")


class BasicSync:
    def __init__(self, rate: Rate = Rate.NORMAL, *, environment: str, api_token: str, worksheet_id: int):
        self.rate = rate
        self.environment = environment
        self.api_token = api_token
        self.worksheet_id = worksheet_id
        self.previous_sync_date = None
        self.config = None
        self.etag = None

    def _get_actual_config(self) -> Optional[ConfigManager]:
        now = datetime.utcnow()

        if self.previous_sync_date and self.config:
            if (now - self.previous_sync_date) < timedelta(seconds=int(self.rate)):
                return self.config

    def get_config(self) -> ConfigManager:
        if actual_config := self._get_actual_config():
            return actual_config

        if self.previous_sync_date and self.config and self.etag:
            response = requests.head(f'{SERVER_HOST}/hash', headers={
                'apiToken': self.api_token,
                'item': str(self.worksheet_id),
                'eTag': self.etag
            })

            # The config is still the same
            #
            if response.status_code == 304:
                return self.config

        response = requests.get(f'{SERVER_HOST}/config', headers={
            'apiToken': self.api_token,
            'item': str(self.worksheet_id)
        })

        if response.status_code == 200:
            raw_data = response.json()
            blob = gzip.decompress(eval(raw_data['config'][self.environment]))  # TODO: Unsafe

            self.config = ConfigManager(config_data=json.loads(blob))
            self.etag = raw_data['eTag']
            self.previous_sync_date = datetime.utcnow()
        elif not self.config:
            raise FipperException(message='Config not available')
        return self.config
