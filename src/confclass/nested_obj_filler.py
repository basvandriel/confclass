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
    def _resolve_obj(self: Self, cls: type, data: dict[str, Any]) -> T:
        obj = cls()
        for k,v in data.items():
            self._validate_class_annotations(Row(obj, k, v), cls.__annotations__)

            if not self._overwrite_defaults:
                try:
                    z = getattr(obj, k)  # It will throw when it can't be found
                    continue
                except:
                    ...
            
            if self._is_nested_object(v):
                innercls: type = cls.__annotations__[k]
                
                self._validate_input_attributes(
                    v, innercls
                )
                v = self._resolve_obj(innercls, v)
            
            setattr(obj, k, v)

        return obj