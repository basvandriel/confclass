from __future__ import annotations

from pathlib import Path
from typing import Type, TypeVar
from configurationclass.configwriter import ConfigWriter, JSONWriter

from configurationclass.main import is_confclass

file_extension_mapper = {
    '.json': JSONWriter()
}

T = TypeVar('T', bound=object)

def parse_config(filepath: Path, type: Type[T]) -> T | None:
    from os import path
    
    if not path.exists(filepath):
        raise FileNotFoundError
    
    if not is_confclass(type):
        raise Exception(f"'{type.__name__}' should be a confclass instance") 
    
    # Find the correct writer
    writer: ConfigWriter | None = file_extension_mapper.get(filepath.suffix)
    
    if writer is None:
        raise Exception(f"No writer found for the '{filepath.suffix}' format")
    
    return writer.read_into(filepath, type)