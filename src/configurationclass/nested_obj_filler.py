from __future__ import annotations

from typing import Any, TypeVar

from configurationclass.flat_object_filler import ObjectFiller
from configurationclass.row import Row
# from configurationclass.flat_object_filler import ObjectFiller, Row


T = TypeVar('T', bound=object)

    
class DataclassFiller(ObjectFiller[T]):
    def _resolve_obj(self, cls: type[T], data: dict[str, Any]) -> T:
        attrs = {}
        
        for k,v in data.items():
            row = Row[T](cls, k, v)
            self._validate_class_annotations(
               row
            )
            if not self._should_set_attr(cls, k):
                continue
            
            attrs[k] = self._resolve_value(row)
            
        return cls(**attrs)