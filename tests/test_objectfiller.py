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
    result: TestingPayload = ObjectFiller(TestingPayload).fill(json)    
        
    assert hasattr(result, 'user')
    assert hasattr(result, 'age')
    assert hasattr(result, 'message')
    

def test_parse_json_defaultvalue_inclass():
    class DefaultedUser:
        user: str = 'Bas'
    
    json = {
        'user': 'NEE',
    } 
    result: DefaultedUser = ObjectFiller(DefaultedUser, False).fill(json)    

    print(result)