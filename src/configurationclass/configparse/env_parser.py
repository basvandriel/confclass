from pathlib import Path
from typing import Any

from . import ConfigParser

from dotenv.main import DotEnv



class EnvFileParser(ConfigParser):
    def read(self, path: Path) -> dict[str, Any]:
        result = DotEnv(path).dict()
        return result