import abc
import json

from pathlib import Path
from typing import Self, TypeVar

from .flat_object_filler import ObjectFiller

T = TypeVar('T', bound=object)


class ConfigWriter(abc.ABC):
    @abc.abstractmethod
    def read_into(self: Self, jsonpath: Path, type: type[T]) -> T:
        ...
    

class JSONWriter(ConfigWriter):
    def read_into(self: Self, jsonpath: Path, type: type[T]) -> T: 
        with open(jsonpath) as jsonfile:
            parsed_json = json.load(jsonfile)
            return ObjectFiller(type).fill(parsed_json)