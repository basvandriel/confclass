
from inspect import isclass
from typing import Any, Self

class ObjectFiller[T: object]:
    __class: type[T]
    __overwrite_defaults: bool
    
    def __init__(self: Self, type: type[T], overwrite_defaults: bool = True) -> None:
        self.__class = type   
        self.__overwrite_defaults = overwrite_defaults
     
    def __should_recurse(self: Self, v: Any) -> bool:
        return type(v) == dict
        
    def __validate_keyval(self: Self, key: str, value: Any, class_annotations: dict[str, Any]):        
        if key not in class_annotations:
            raise Exception(f"Attribute '{key}' not found in class")
                 
        isinner: bool = isclass(class_annotations[key])
        
        # A dict should be a class instance
        if (type(value) != class_annotations[key]) and not isinner:
            raise Exception(f'Type mismatch for {key} attribute')
        
    def __keep_default(self: Self, obj: object, key: str):
        _ = getattr(obj, key)
        
    def __process_inner(self: Self, attributes: dict[str, Any], t: type):
        """Annotation key""" 
        obj = t()

        for k,v in attributes.items():       
            self.__validate_keyval(k, v, t.__annotations__)            
            
            if self.__should_recurse(v):
                cls = t.__annotations__[k]
                v = self.__process_inner(v, cls) # type: ignore
            
            setattr(obj, k, v)
        
        return obj
    
    def __process_data(self: Self, obj: object, key: str, value: Any):  
        # TODO it should also fail when it's missing properties.
        # Currently, only functions when it has the attribute in the dict,
        # but not in the class annotations. Should be bi-directional.  
        # 
        # Maybe make a difference between the validated attributes? 😄
        self.__validate_keyval(key, value, self.__class.__annotations__)
        
        if not self.__overwrite_defaults:
            try:
                self.__keep_default(obj, key)
                return
            except:
                ...
                
        if self.__should_recurse(value):
            inner_obj = self.__process_inner(value, self.__class.__annotations__[key]) # type: ignore
            
            # So we don't have to call setattr multiple times, and it should be an object
            value = inner_obj

        setattr(obj, key, value)
            
            
    def fill(self: Self, data: dict[str, Any]) -> T:
        obj = self.__class()

        for k,v in data.items():
            self.__process_data(obj, k, v)
            
        return obj
    
    