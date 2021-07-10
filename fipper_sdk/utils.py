from enum import IntEnum


SERVER_HOST = 'https://sync.fipper.io'

class Rate(IntEnum):
    RARELY = 15
    NORMAL = 7
    FREQUENTLY = 3


class FlagType(IntEnum):
    BOOLEAN = 10
    INTEGER = 20
    STRING = 30
    JSON = 40
