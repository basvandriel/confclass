from pathlib import Path
from configurationclass.configparse.env_parser import EnvFileParser


def test_env_parse_ok(testdir: Path):
    result = EnvFileParser().read(testdir / 'test.env')
    assert result == {'USER': 'bas', 'AGE': '29'}