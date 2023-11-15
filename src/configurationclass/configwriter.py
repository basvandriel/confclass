from __future__ import annotations

import abc, json

from pathlib import Path
from typing import Any, TypeVar

T = TypeVar('T', bound=object)

class ConfigParser(abc.ABC):
    @abc.abstractmethod
    def read(self, path: Path) -> dict[str, Any]:
        ...

class JSONConfigParser(ConfigParser):
    def read(self, path: Path) -> dict[str, Any]:
        with open(path) as jsonfile:
            return json.load(jsonfile) # type: ignore