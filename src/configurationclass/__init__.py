from dataclasses import is_dataclass
from inspect import isclass
from pathlib import Path
from typing import Type, TypeVar

from configurationclass.nested_obj_filler import DataclassFiller

T = TypeVar('T', bound=object)

def confclass(cls: T) -> T:
    if cls is None:
        raise ValueError("Decorator can only be used with parameters")
    if not isclass(cls):
        raise ValueError("Decorator can only be used on a class")

    def wrap(cls: T): # type: ignore 
        setattr(cls, '__IS_CONCLASS__', True) 
        return cls

    return wrap(cls) # type: ignore


def parse_dataclass(filepath: Path, type: Type[T]) -> T | None:
    from os import path
    
    if not path.exists(filepath):
        raise FileNotFoundError
    
    if not is_dataclass(type):
        raise Exception(f"'{type.__name__}' should be a dataclass instance") 
    
    # only JSON support
    import json
    
    file = open(filepath, 'r')
    attrs =  json.load(file)
    
    result = DataclassFiller(type).fill(attrs)
    
    return result # type: ignore