from enum import Enum


class UpdateGroupParticipantsAction(str, Enum):
    ADD = "add"
    DEMOTE = "demote"
    PROMOTE = "promote"
    REMOVE = "remove"

    def __str__(self) -> str:
        return str(self.value)
