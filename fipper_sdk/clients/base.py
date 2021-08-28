from datetime import datetime, timedelta
from typing import Optional

from fipper_sdk.manager import ConfigManager
from fipper_sdk.utils import Rate


class BaseClient:
    def __init__(self, rate: Rate = Rate.NORMAL, *, environment: str, api_token: str, project_id: int):
        self.rate = rate
        self.environment = environment
        self.api_token = api_token
        self.project_id = project_id
        self.previous_sync_date = None
        self.config = None
        self.etag = None

    def _get_actual_config(self) -> Optional[ConfigManager]:
        now = datetime.utcnow()

        if self.previous_sync_date and self.config:
            if (now - self.previous_sync_date) < timedelta(seconds=int(self.rate)):
                return self.config
