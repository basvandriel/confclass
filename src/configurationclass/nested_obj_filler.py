from typing import Any, Self
from configurationclass.flat_object_filler import ObjectFiller, Row


class ComplexObjectFiller[T: object](ObjectFiller[T]):   
    ...
    
class DataclassFiller[DT: object](ObjectFiller[DT]):
    def _resolve_obj(self: Self, cls: type, data: dict[str, Any]) -> DT:
        attrs = {}
        
        for k,v in data.items():
            self._validate_class_annotations(
                (row := Row(cls, k, v))
            )
            if not self._should_set_attr(cls, k):
                continue
            
            attrs[k] = self._resolve_value(row)
            
        return cls(**attrs)