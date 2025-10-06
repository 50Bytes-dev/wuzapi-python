from enum import Enum


class GroupEphemeralDuration(str, Enum):
    OFF = "off"
    VALUE_0 = "24h"
    VALUE_1 = "7d"
    VALUE_2 = "90d"

    def __str__(self) -> str:
        return str(self.value)
