from enum import IntEnum
from typing import Iterable, Tuple


class UserPaymentStatus(IntEnum):

    CREATED = 0
    DONE = 1
    ERROR = 2

    @classmethod
    def choices(cls) -> Iterable[Tuple[int, str]]:
        return ((key.value, key.name) for key in cls)