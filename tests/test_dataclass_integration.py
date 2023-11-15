from dataclasses import dataclass
from configurationclass import parse_dataclass
from pathlib import Path

def test_notnone(testdir: Path):
    @dataclass
    class User:
        name: str
        age: int
        
    filepath = testdir / 'test.json'

    result = parse_dataclass(filepath, User)
    
    assert result is not None
    assert result.age == 29