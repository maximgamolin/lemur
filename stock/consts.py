from enum import IntEnum
from typing import Iterable, Tuple


class DatasetStatus(IntEnum):

    CREATED = 0
    AVAILABLE = 1

    @classmethod
    def choices(cls) -> Iterable[Tuple[int, str]]:
        return ((key.value, key.name) for key in cls)


class DatasetPriceCurrency(IntEnum):

    RUB = 0

    @classmethod
    def choices(cls) -> Iterable[Tuple[int, str]]:
        return ((key.value, key.name) for key in cls)

