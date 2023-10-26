import abc
import json

from pathlib import Path
from typing import Self

from confclass.object_filler import ObjectFiller

class ConfigWriter(abc.ABC):
    @abc.abstractmethod
    def read_into[T](self: Self, jsonpath: Path, type: type[T]) -> T:
        ...
    

class JSONWriter(ConfigWriter):
    def read_into[T](self: Self, jsonpath: Path, type: type[T]) -> T: 
        with open(jsonpath) as jsonfile:
            parsed_json = json.load(jsonfile)
            return ObjectFiller(type).fill(parsed_json)