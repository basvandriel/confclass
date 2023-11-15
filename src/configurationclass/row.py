

from dataclasses import dataclass
from typing import Any, Generic, Type, TypeVar

T = TypeVar('T', bound=object)

@dataclass
class Row(Generic[T]):
    type: Type[T]
    key: str
    value: Any
    
    @property
    def valuetype(self) -> Type[Any]:
        attrs = self.type.__annotations__
        return attrs[self.key] # type: ignore[no-any-return]