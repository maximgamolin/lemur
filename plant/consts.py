from enum import IntEnum
from typing import Iterable, Tuple


class WorkpieceStatus(IntEnum):

    CREATED = 0
    FINISHED = 1

    @classmethod
    def choices(cls) -> Iterable[Tuple[int, str]]:
        return ((key.value, key.name) for key in cls)


class JoinType(IntEnum):

    INNER = 0
    LEFT = 1
    RIGHT = 2

    @classmethod
    def choices(cls) -> Iterable[Tuple[int, str]]:
        return ((key.value, key.name) for key in cls)
