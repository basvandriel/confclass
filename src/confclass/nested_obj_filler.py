from inspect import isclass
from typing import Any, Self, override
from confclass.flat_object_filler import ObjectFiller, Row


class ComplexObjectFiller[T: object](ObjectFiller[T]):   
    @override 
    def _validate_class_annotations(self: Self, row: Row[T], class_annotations: dict[str, Any]):
        if row.key not in class_annotations:
            raise Exception(f"Attribute '{row.key}' not found in class")
                        
        isinner: bool = isclass(class_annotations[row.key])
        if (type(row.value) != class_annotations[row.key]) and not isinner:
            raise Exception(f'Type mismatch for {row.key} attribute')
        
    
    @override
    def _resolve_value(self: Self, row: Row[T]) -> Any:
        if not self._is_nested_object(row.value):
            return row.value
    
        innercls: type = row.type.__annotations__[row.key]
        
        self._validate_input_attributes(
            row.value, innercls
        )
        return self._resolve_obj(innercls, row.value)
    
    
class DataclassFiller[DT: object](ComplexObjectFiller[DT]):
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