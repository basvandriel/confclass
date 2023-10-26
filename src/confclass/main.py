from typing import Any, Self


class Configuration:
    def hi(self):
        print('hi')
    
def confclass(obj: object):
    obj.CONFCLASS_NAME = 'confclass'
    
    # T = obj.__class__
    # class K(Configuration, T):
    #     ...
    t: Configuration =  type(obj.__name__, (Configuration, obj), {})
    return t

def is_confclass(obj: object) -> bool:
    return hasattr(obj, 'CONFCLASS_NAME') and isinstance(confclass, Configuration)


def get_configuration(confclass: object) -> Configuration | None:
    return confclass if is_confclass(confclass) else None


class ObjectFiller[T: object]:
    __obj: T
    
    def __init__(self: Self, obj: T) -> None:
        self.__obj = obj   
        
    def __validate_keyval(self: Self, key: str, value: Any):
        attrs = self.__obj.__annotations__
        
        if key not in attrs:
            raise Exception('Attribute not found in class')
                
        if type(value) != attrs[key]:
            raise Exception(f'Type mismatch for {key} attribute')
    
    def __process_data(self: Self, key, value):
        self.__validate_keyval(key, value)
        setattr(self.__obj, key, value)
            
    def fill(self: Self, data: dict[str, Any]) -> T:
        [
            self.__process_data(k,v) for k, v in data.items()
        ]
        return self.__obj
