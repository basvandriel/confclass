from dataclasses import dataclass
from typing import Any


@dataclass
class Row[T: object]:
    type: type[T]
    key: str
    value: Any