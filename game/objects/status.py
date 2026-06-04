from enum import Enum
from typing import Optional


class Status(Enum):
    NORMAL = "normal"
    SLEEPING = "sleeping"
    CONFUSED = "confused"
    POISONED = "poisoned"

StatusChange = tuple[Status, Status]

StatusChangeResult = tuple[Optional[StatusChange], Optional[StatusChange]]