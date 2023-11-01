


from typing import Any
from pytest import raises
from confclass.object_filler import ObjectFiller


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
    result: TestingPayload = ObjectFiller(TestingPayload).fill(json)    
        
    assert hasattr(result, 'user')
    assert hasattr(result, 'age')
    assert hasattr(result, 'message')
    

def test_parse_json_defaultvalue_inclass():
    class DefaultedUser:
        name: str = 'Bas'
    
    result: DefaultedUser = ObjectFiller(DefaultedUser, False).fill({'name': 'NEE' })    

    assert result is not None
    assert result.name == 'Bas'
    
def test_require_all_annotations_one_miss():
    json = {
        'user': 'Bas',
        'age': 23,
    }
    with raises(Exception) as e: 
        ObjectFiller(TestingPayload).fill(json)   
        
    assert str(e.value) == "Missing input attributes: message"

def test_require_all_annotations_multi_miss():
    json = {
        'user': 'Bas',
    }
    with raises(Exception) as e: 
        ObjectFiller(TestingPayload).fill(json)   
        
    assert str(e.value) == "Missing input attributes: age, message"
    
def test_require_all_annotations_multi_inner_miss():
    class Foo:
        bar: str
        baz: str
        
    class TestingInput(TestingPayload):
        user: str
        age: int
        message: str
        foo: Foo
    
    data: dict[str, Any] = {
        'user': 'Bas',
        'age': 23,
        'message': 'Hi there',
        'foo': {}
    }
    with raises(Exception) as e: 
        ObjectFiller(TestingInput).fill(data)   
        
    assert str(e.value) == 'Missing input attributes: bar, baz'