from dataclasses import dataclass
from confclass.main import ObjectFiller

class TestingPayload:
    user: str
    age: int
    message: str


def test_parse_json():
    json = {
        'user': 'Bas',
        'age': 23,
        'message': 'Hi there'
    }    
    
    result = ObjectFiller(TestingPayload()).fill(json)
        
    assert hasattr(result, 'user')
    assert hasattr(result, 'age')
    assert hasattr(result, 'message')