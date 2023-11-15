from __future__ import annotations

import json

from pathlib import Path
from typing import Any, TypeVar

from . import ConfigParser

T = TypeVar('T', bound=object)

class JSONConfigParser(ConfigParser):
    def read(self, path: Path) -> dict[str, Any]:
        with open(path) as jsonfile:
            return json.load(jsonfile) # type: ignore