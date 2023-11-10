


from typing import Any
from pytest import raises
from configurationclass.nested_obj_filler import ComplexObjectFiller, ObjectFiller
# from confclass.object_filler import ObjectFiller


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
    
def test_parse_json_default_value_nested():
    class Address:
        street: str = "street"
    
    class User:
        address: Address
    
    result: User = ComplexObjectFiller(User, False).fill({'address': {'street': 'nooo'} })    

    assert result.address.street == 'street'
    
    
def test_require_all_annotations_one_miss():
    json = {
        'user': 'Bas',
        'age': 23,
    }
    with raises(Exception) as e: 
        ObjectFiller(TestingPayload).fill(json)   
        
    assert str(e.value) == "Missing input attributes for TestingPayload: message"

def test_require_all_annotations_multi_miss():
    json = {
        'user': 'Bas',
    }
    with raises(Exception) as e: 
        ObjectFiller(TestingPayload).fill(json)   
        
    assert str(e.value) == "Missing input attributes for TestingPayload: age, message"
    
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
        ComplexObjectFiller(TestingInput).fill(data)   
        
    assert str(e.value) == 'Missing input attributes for Foo: bar, baz'