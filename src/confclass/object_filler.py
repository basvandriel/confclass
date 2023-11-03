
from inspect import isclass
from typing import Any, Self

class ObjectFiller[T: object]:
    _class: type[T]
    _overwrite_defaults: bool
    
    def __init__(self: Self, type: type[T], overwrite_defaults: bool = True) -> None:
        self._class = type   
        self._overwrite_defaults = overwrite_defaults
     
    def __should_recurse(self: Self, v: Any) -> bool:
        return type(v) == dict
        
    def __validate_class_annotations(self: Self, key: str, value: Any, class_annotations: dict[str, Any]):        
        if key not in class_annotations:
            raise Exception(f"Attribute '{key}' not found in class")
                 
        isinner: bool = isclass(class_annotations[key])
        
        # A dict should be a class instance
        if (type(value) != class_annotations[key]) and not isinner:
            raise Exception(f'Type mismatch for {key} attribute')
        

    def __process_inner(self: Self, attributes: dict[str, Any], t: type):
        """Annotation key""" 
        self.__validate_input_attributes(
            attributes, t
        )
        obj = t()

        for k,v in attributes.items():       
            self.__validate_class_annotations(k, v, t.__annotations__)       
             
            if not self._overwrite_defaults:
                try:
                    getattr(obj, k) # It will throw when it can't be found
                    continue
                except:
                    ...
                    
            if self.__should_recurse(v):
                cls = t.__annotations__[k]
                v = self.__process_inner(v, cls) # type: ignore
            
            setattr(obj, k, v)
        
        return obj
    
    def __process_data(self: Self, obj: object, key: str, value: Any):  
        self.__validate_class_annotations(key, value, self._class.__annotations__)
        
        if not self._overwrite_defaults:
            try:
                getattr(obj, key) # It will throw when it can't be found
                return
            except:
                ...
                
        if self.__should_recurse(value):
            value = self.__process_inner(value, self._class.__annotations__[key]) # type: ignore

        setattr(obj, key, value)

    def __validate_input_attributes(
        self: Self, data: dict[str, Any], matching_class: type[Any]
    ):
        classname: str = matching_class.__name__
        expected: list[str] = list(matching_class.__annotations__.keys())
        
        diff = [x for x in expected if x not in set(data.keys())]
        
        if len(diff) != 0:
            msg = f"Missing input attributes for {classname}: {', '.join(diff)}"
            raise Exception(msg)

            
    def fill(self: Self, data: dict[str, Any]) -> T:
        # TODO this doesn't work with inheritance
        self.__validate_input_attributes(
            data, self._class
        )
        obj = self._class()
        [self.__process_data(obj, k, v) for k, v in data.items()]
            
        return obj
    
    