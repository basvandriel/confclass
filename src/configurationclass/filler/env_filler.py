from __future__ import annotations

from typing import Any, Type, TypeVar, override
from configurationclass.filler.flat_object_filler import ObjectFiller
from configurationclass.row import Row

T = TypeVar('T', bound=object)

class EnvObjectFiller(ObjectFiller[T]):
    # There are configuration formats which always 
    # read as a string. Lets cast :D
    __cast_to_type_annotations: bool

    def __init__(self, type: type[T], overwrite_defaults: bool = True, cast_to_type_annotations: bool = True) -> None:
        super().__init__(type, overwrite_defaults)
        self.__cast_to_type_annotations = cast_to_type_annotations
        
    # TODO type cast from type annotation
    # TODO don't inherit from nested structure fillers.


    @override
    def _resolve_obj(self, cls: Type[T], data: dict[str, Any]) -> T:
        obj = cls()
        
        for k,v in data.items():
            row = Row[T](cls, k, v)
            self._validate_class_annotations(
                row
            )
            if not self._should_set_attr(cls, k):
                continue
                        
            setattr(obj, k, self._resolve_value(row))
            
        return obj