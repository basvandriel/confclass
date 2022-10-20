from dataclasses import is_dataclass
import enum

from .processor import ClassProcessor

import inspect
class ConfigurationType(enum.Enum):
    ...

def confclass(cls: object | None = None, /):    
    # When confclass is called without "()" (@confclass), an error should appear
    # In that case, cls is filled in
    if cls is not None:
        raise ValueError('Decorator can only be used with parameters')
    
    def wrap(cls):
        if not inspect.isclass(cls):
            raise ValueError('Decorator can only be used on a class')
        
        return ClassProcessor().process(cls)

    return wrap
