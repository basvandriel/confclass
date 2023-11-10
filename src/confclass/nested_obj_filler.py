from typing import Any, Self
from confclass.flat_object_filler import ObjectFiller, Row


class ComplexObjectFiller[T: object](ObjectFiller[T]):   
    ...
    
class DataclassFiller[DT: object](ObjectFiller[DT]):
    def __should_set_attr(self: Self, cls: type, k: str):
        return self._overwrite_defaults or not hasattr(cls, k)
    
    def _resolve_obj(self: Self, cls: type, data: dict[str, Any]) -> DT:
        attrs = {}
        
        for k,v in data.items():
            self._validate_class_annotations(
                (row := Row(cls, k, v)), cls.__annotations__
            )
            if not self.__should_set_attr(cls, k):
                continue
            
            attrs[k] = self._resolve_value(row)
            
        return cls(**attrs)