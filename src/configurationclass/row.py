from dataclasses import dataclass
from typing import Any, Generic, TypeVar

T = TypeVar('T', bound=object)

@dataclass
class Row(Generic[T]):
    type: type[T]
    key: str
    value: Any