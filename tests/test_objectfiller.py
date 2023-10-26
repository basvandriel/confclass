


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