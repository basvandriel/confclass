
from typing import Any, Self


class ObjectFiller[T: object]:
    __class: type[T]
    __overwrite_defaults: bool
    
    def __init__(self: Self, type: type[T], overwrite_defaults: bool = True) -> None:
        self.__class = type   
        self.__overwrite_defaults = overwrite_defaults
        
    def __validate_keyval(self: Self, key: str, value: Any):
        attrs = self.__class.__annotations__
        
        if key not in attrs:
            raise Exception('Attribute not found in class')
                
        if type(value) != attrs[key]:
            raise Exception(f'Type mismatch for {key} attribute')
        
    def __keep_default(self: Self, obj: object, key: str):
        _ = getattr(obj, key)
    
    def __process_data(self: Self, obj: object, key: str, value: Any):    
        self.__validate_keyval(key, value)
        
        if not self.__overwrite_defaults:
            try:
                self.__keep_default(obj, key)
                return
            except:
                ...
            
        setattr(obj, key, value)

            
    def fill(self: Self, data: dict[str, Any]) -> T:
        obj = self.__class()

        for k,v in data.items():
            self.__process_data(obj, k, v)
            
        return obj