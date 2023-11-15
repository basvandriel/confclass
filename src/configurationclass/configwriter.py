from __future__ import annotations

import abc
import json

from pathlib import Path
from typing import Type, TypeVar

from .flat_object_filler import ObjectFiller

T = TypeVar('T', bound=object)


class ConfigWriter(abc.ABC):
    @abc.abstractmethod
    def read_into(self, jsonpath: Path, type: Type[T]) -> T:
        ...
    

class JSONWriter(ConfigWriter):
    def read_into(self, jsonpath: Path, type: Type[T]) -> T: 
        with open(jsonpath) as jsonfile:
            parsed_json = json.load(jsonfile)
            
            return ObjectFiller(type).fill(parsed_json)