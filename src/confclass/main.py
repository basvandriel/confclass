from pathlib import Path
from typing import Any, Self
import json


class Configuration:
    def hi(self):
        print('hi')
    

    

def is_confclass(obj: object) -> bool:
    return hasattr(obj, '__IS_CONCLASS__')

class ObjectFiller[T: object]:
    __class: type[T]
    
    def __init__(self: Self, type: type[T]) -> None:
        self.__class = type   
        
    def __validate_keyval(self: Self, key: str, value: Any):
        attrs = self.__class.__annotations__
        
        if key not in attrs:
            raise Exception('Attribute not found in class')
                
        if type(value) != attrs[key]:
            raise Exception(f'Type mismatch for {key} attribute')
    
    def __process_data(self: Self, obj: object, key: str, value: Any):
        self.__validate_keyval(key, value)
        setattr(obj, key, value)
            
    def fill(self: Self, data: dict[str, Any]) -> T:
        obj = self.__class()
        type[T]
        [
            self.__process_data(obj, k, v) for k, v in data.items()
        ]
        
        return obj
    
    

class JSONConfigReader:
    def read_into[T](self: Self, jsonpath: Path, type: type[T]) -> T: 
        with open(jsonpath) as jsonfile:
            parsed_json = json.load(jsonfile)
            return ObjectFiller(type).fill(parsed_json)
    
    
    



def parse_config[T: object](jsonpath: Path, type: type[T]) -> T | None: 
    if not is_confclass(type):
        raise Exception(f"'{type.__name__}' should be a confclass instance") # type: ignore
    
    r = JSONConfigReader().read_into(jsonpath, type)
    
    return r