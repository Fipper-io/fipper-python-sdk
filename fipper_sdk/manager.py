import json
from typing import Any

from fipper_sdk.utils import FlagType


class Flag:
    __slots__ = ('slug', 'flag_type', 'state', 'value')

    def __init__(self, slug: str, flag_type: FlagType, state: bool, value: Any):
        self.slug = slug
        self.flag_type = flag_type
        self.state = state
        self.value = value

    def get_value(self):
        if self.flag_type == FlagType.BOOLEAN:
            return bool(self.state)
        elif self.flag_type == FlagType.INTEGER:
            return int(self.value)
        elif self.flag_type == FlagType.STRING:
            return str(self.value)
        elif self.flag_type == FlagType.JSON:
            return json.loads(self.value)
        raise ValueError()


class ConfigManager:
    __slots__ = ('config_data',)

    def __init__(self, config_data: dict):
        self.config_data = dict()

        for slug, payload in config_data.items():
            self.config_data[slug] = Flag(
                slug,
                FlagType(payload['type']),
                payload['state'],
                payload['value']
            )

    def __getitem__(self, item):
        return self.config_data[item]
