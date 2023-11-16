from __future__ import annotations

from typing import Any, Type, TypeVar, override
from configurationclass.filler.flat_object_filler import FlatObjectfiller
from configurationclass.row import Row

T = TypeVar('T', bound=object)

class CastingObjectFiller(FlatObjectfiller[T]):
    # There are configuration formats which always 
    # read as a string. Lets cast :D
    __SUPPORTED_CAST_TYPES = str | int | float
        
    def __cast_from_row(self, row: Row[T]) -> __SUPPORTED_CAST_TYPES:
        expected_type: Type[Any] = row.valuetype
        caster:  Type[float | int | str] = expected_type
        
        return caster(row.value)
    
    @override
    def _resolve_obj(self, cls: Type[T], data: dict[str, Any]) -> T:
        obj = cls()
    
        for k,v in data.items():
            if not self._should_set_attr(cls, k): continue
            row = Row[T](cls, k, v)
            
            type_mismatch: bool = row.valuetype != type(v)
            can_cast: bool = (
                isinstance(row.value, self.__SUPPORTED_CAST_TYPES) # type: ignore[arg-type]
            )
            if type_mismatch and can_cast:
                row.value = self.__cast_from_row(row)
            
            setattr(obj, k, row.value)
            
        return obj