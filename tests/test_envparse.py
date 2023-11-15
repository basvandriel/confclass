from pathlib import Path
from configurationclass.configparse.env_parser import EnvFileParser
from configurationclass.filler.env_filler import EnvObjectFiller


def test_env_parse_ok(testdir: Path):
    result = EnvFileParser().read(testdir / 'test.env')
    assert result == {'USER': 'bas', 'AGE': '29'}

# EnvObjectFiller
def test_env_filler():
    class User:
        name: str
        age: int
    
    
    filler = EnvObjectFiller(User)
    x = filler.fill({
        'name': 'Bas',
        'age': '200'
    })
    
    print(1)