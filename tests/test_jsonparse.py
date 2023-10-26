from pathlib import Path

from confclass.configwriter import JSONWriter

class TestingPayload:
    name: str
    age: int
    
def test_jsonparse(testdir: Path):
    filepath = testdir / 'test.json'
    result: TestingPayload = JSONWriter().read_into(filepath, TestingPayload)

    assert 1 == 1