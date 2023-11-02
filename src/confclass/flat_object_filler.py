from typing import Any, Self


class ObjectFiller[T: object]:
    __class: type[T]
    __overwrite_defaults: bool
    
    def __init__(self: Self, type: type[T], overwrite_defaults: bool = True) -> None:
        self.__class = type   
        self.__overwrite_defaults = overwrite_defaults
        
    def __is_nested_object(self: Self, v: Any) -> bool:
        return type(v) == dict
     
    def __validate_input_attributes(
        self: Self, data: dict[str, Any], matching_class: type[Any]
    ):
        classname: str = matching_class.__name__
        expected: list[str] = list(matching_class.__annotations__.keys())
        
        diff = [x for x in expected if x not in set(data.keys())]
        
        if len(diff) != 0:
            msg = f"Missing input attributes for {classname}: {', '.join(diff)}"
            raise Exception(msg)

    def __validate_class_annotations(self: Self, key: str, value: Any, class_annotations: dict[str, Any]):
        if self.__is_nested_object(value):
            raise Exception('Only flat structures are supported')
        
        if key not in class_annotations:
            raise Exception(f"Attribute '{key}' not found in class")
                        
        if (type(value) != class_annotations[key]):
            raise Exception(f'Type mismatch for {key} attribute')
        
    def __validate_row(self: Self, obj: object, key: str, value: Any) -> None:  
        self.__validate_class_annotations(key, value, self.__class.__annotations__)
        
        if not self.__overwrite_defaults:
            try:
                getattr(obj, key) # It will throw when it can't be found
            except:
                raise
        
    def __resolve_obj(self: Self, type: type[T], data: dict[str, Any]) -> T:
        obj = self.__class()
        for k,v in data.items():
            try:
                self.__validate_row(
                    obj, k, v
                )
                setattr(obj, k, v)
            except:
                continue
        
        return obj

    def fill(self: Self, data: dict[str, Any]) -> T:
        self.__validate_input_attributes(
            data, self.__class
        )
        return self.__resolve_obj(self.__class, data)