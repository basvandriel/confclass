from __future__ import annotations

import abc
import json

from pathlib import Path
from typing import Any, Type, TypeVar

from .flat_object_filler import ObjectFiller

T = TypeVar('T', bound=object)


class ConfigParser(abc.ABC):
    @abc.abstractmethod
    def read(self, path: Path) -> dict[str, Any]:
        ...

class JSONConfigParser(ConfigParser):
    def read(self, path: Path) -> dict[str, Any]:
        with open(path) as jsonfile:
            return json.load(jsonfile) # type: ignore

class ConfigWriter(abc.ABC):
    @abc.abstractmethod
    def read_into(self, jsonpath: Path, type: Type[T]) -> T:
        ...
    

class JSONWriter(ConfigWriter):
    def read_into(self, jsonpath: Path, type: Type[T]) -> T: 
        json = JSONConfigParser().read(jsonpath)
        return ObjectFiller(type).fill(json)