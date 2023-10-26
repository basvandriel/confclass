from pathlib import Path
from confclass.main import JSONConfigReader

class TestingPayload:
    name: str
    age: int
    
def test_jsonparse(testdir: Path):
    filepath = testdir / 'test.json'
    result = JSONConfigReader().read_into(filepath, TestingPayload)

    assert 1 == 1