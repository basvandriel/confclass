from pathlib import Path
from confclass.configwriter import ConfigWriter, JSONWriter

from confclass.main import is_confclass

file_extension_mapper = {
    '.json': JSONWriter()
}
def parse_config[T: object](filepath: Path, type: type[T]) -> T | None: 
    from os import path
    
    if not path.exists(filepath):
        raise FileNotFoundError
    
    if not is_confclass(type):
        raise Exception(f"'{type.__name__}' should be a confclass instance") # type: ignore
    
    # Find the correct writer
    writer: ConfigWriter | None = file_extension_mapper.get(filepath.suffix)
    
    if writer is None:
        raise Exception(f"No writer found for the '{filepath.suffix}' format")
    
    return writer.read_into(filepath, type)