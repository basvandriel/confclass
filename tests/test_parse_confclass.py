from pathlib import Path
from confclass import confclass
from confclass.main import parse_config
from pytest import raises

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
    