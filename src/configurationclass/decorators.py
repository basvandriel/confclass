from __future__ import annotations

from pathlib import Path
from typing import Type, TypeVar
from configurationclass.configwriter import JSONConfigParser
from os import path

from . import load_dict_in_confclass

T = TypeVar('T', bound=object)

def parse_config(filepath: Path, type: Type[T]) -> T | None:
    if not path.exists(filepath):
        raise FileNotFoundError
    
    # only JSON support currently
    attrs = JSONConfigParser().read(filepath)
    
    return load_dict_in_confclass(attrs, type)