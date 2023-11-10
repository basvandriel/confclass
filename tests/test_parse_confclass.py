from pathlib import Path
from configurationclass import confclass
from pytest import raises

from configurationclass.decorators import parse_config

@confclass
class Person:
    name: str
    age: int
    
def test_parse_confclass_no_decorator(testdir: Path):
    class TestingPayload:
        name: str

    with raises(Exception) as e:
        parse_config(testdir / "test.json", TestingPayload)
        
    assert str(e.value) == "'TestingPayload' should be a confclass instance"


def test_parse_filenotfound(testdir: Path):
    with raises(Exception) as e:
        parse_config(testdir / "test_notfound.json", Person)

    assert e.typename == 'FileNotFoundError'
    