from enum import IntEnum
from typing import Iterable, Tuple


class SchemaBlockCategory(IntEnum):

    MATH = 0
    STRINGS = 1

    @classmethod
    def choices(cls) -> Iterable[Tuple[int, str]]:
        return ((key.value, key.name) for key in cls)


class SchemaBlockType(IntEnum):

    COMMON = 0
    FILTER = 1
    FEATURE = 2
    JOIN = 3

    @classmethod
    def choices(cls) -> Iterable[Tuple[int, str]]:
        return ((key.value, key.name) for key in cls)
