
from inspect import isclass
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
                
        
        isinner: bool = isclass(attrs[key])
        
        # A dict should be a class instance
        if (type(value) != attrs[key]) and not isinner:
            raise Exception(f'Type mismatch for {key} attribute')
        
    def __keep_default(self: Self, obj: object, key: str):
        _ = getattr(obj, key)
        
    def __process_inner(self: Self, attributes: dict[str, Any], t: type):
        """Annotation key"""
        obj = t()

        for k,v in attributes.items():
            should_recurse = type(v) == dict
            if should_recurse:
                # k = self.__class.__annotations__[key]
                v = self.__process_inner(v, t.__annotations__[k]) # type: ignore
            
            setattr(obj, k, v)
        
        return obj
    
    def __process_data(self: Self, obj: object, key: str, value: Any):    
        self.__validate_keyval(key, value)
        
        if not self.__overwrite_defaults:
            try:
                self.__keep_default(obj, key)
                return
            except:
                ...
                
        if type(value) == dict:
            inner_obj = self.__process_inner(value, self.__class.__annotations__[key]) # type: ignore
            
            # So we don't have to call setattr multiple times, and it should be an object
            value = inner_obj

        setattr(obj, key, value)
            

            
    def fill(self: Self, data: dict[str, Any]) -> T:
        obj = self.__class()

        for k,v in data.items():
            self.__process_data(obj, k, v)
            
        return obj
    
    