from inspect import isclass
from typing import TypeVar

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
