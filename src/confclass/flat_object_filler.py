from dataclasses import dataclass
from typing import Any, Self

        
@dataclass
class Row[RT: object]:
    type: type[RT]
    key: str
    value: Any

class ObjectFiller[T: object]:
    _class: type[T]
    _overwrite_defaults: bool
    
    def __init__(self: Self, type: type[T], overwrite_defaults: bool = True) -> None:
        self._class = type   
        self._overwrite_defaults = overwrite_defaults
        
    def _is_nested_object(self: Self, v: Any) -> bool:
        return type(v) == dict
     
    def _validate_input_attributes(
        self: Self, data: dict[str, Any], matching_class: type[Any]
    ):
        classname: str = matching_class.__name__
        expected: list[str] = list(matching_class.__annotations__.keys())

        diff = [x for x in expected if x not in set(data.keys())]

        if diff:
            msg = f"Missing input attributes for {classname}: {', '.join(diff)}"
            raise Exception(msg)

    def _validate_class_annotations(self: Self, row: Row[T], class_annotations: dict[str, Any]):
        if self._is_nested_object(row.value):
            raise Exception('Only flat structures are supported')
        
        if row.key not in class_annotations:
            raise Exception(f"Attribute '{row.key}' not found in class")
                        
        if (type(row.value) != class_annotations[row.key]):
            raise Exception(f'Type mismatch for {row.key} attribute')
        

    def _resolve_value(self: Self, row: Row[T]) -> Any:
        return row.value

    def _resolve_obj(self: Self, cls: type, data: dict[str, Any]) -> T:
        obj = cls()
        for k,v in data.items():
            row = Row(
                cls, k, v
            )
            self._validate_class_annotations(row, cls.__annotations__)

            if not self._overwrite_defaults and hasattr(obj, k):
                continue
                        
            setattr(obj, k, self._resolve_value(row))
            
        return obj

    def fill(self: Self, data: dict[str, Any]) -> T:
        self._validate_input_attributes(
            data, self._class
        )
        return self._resolve_obj(self._class, data)