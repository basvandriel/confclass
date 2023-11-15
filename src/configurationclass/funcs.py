from __future__ import annotations

from dataclasses import is_dataclass
from pathlib import Path
from typing import Any, Type, TypeVar
from configurationclass.configparse.json_parser import JSONConfigParser

from .filler.nested_obj_filler import DataclassFiller
from .filler.flat_object_filler import ObjectFiller

from os import path


T = TypeVar('T', bound=object)

def is_confclass(obj: object) -> bool:
    return hasattr(obj, '__IS_CONCLASS__')
    

def dict_in_dataclass(data: dict[str, Any], type: Type[T]) -> T | None:
    if not is_dataclass(type):
        raise SyntaxError(f"'{type.__name__}' should be a dataclass instance")
    return DataclassFiller(type).fill(data) # type: ignore[return-value]

def dict_in_confclass(data: dict[str, Any], type: Type[T]) -> T | None:
    if not is_confclass(type):
        raise SyntaxError(f"'{type.__name__}' should be a confclass instance") 
    return ObjectFiller(type).fill(data)

def parse_dataclass(filepath: Path, type: Type[T]) -> T | None:
    if not path.exists(filepath):
        raise FileNotFoundError
    
    # only JSON support currently
    attrs = JSONConfigParser().read(filepath)
    
    return dict_in_dataclass(attrs, type)

def parse_config(filepath: Path, type: Type[T]) -> T | None:
    if not path.exists(filepath):
        raise FileNotFoundError
    
    # only JSON support currently
    attrs = JSONConfigParser().read(filepath)
    
    return dict_in_confclass(attrs, type)