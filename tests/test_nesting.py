from pytest import raises
from configurationclass.nested_obj_filler import ObjectFiller
    
def test_1level_basic_nest():
    class Adress:
        street: str
        city: str

    class User:
        name: str
        age: int
        address: Adress
        
    json = {
        'name': 'Bas',
        'age': 22,
        'address': {
            'street': 'city',
            'city': 'street'
        }
    }
    x = ObjectFiller(User).fill(json)    
    assert x.address != None
    assert x.address.city == 'street'
    
    
def test_2level_nest():
    class Postal:
        numbers: str
        suffix: str
    
    class Adress:
        street: str
        city: str
        postal: Postal        

    class User:
        address: Adress
        
    json = {
        'address': {
            'street': 'city',
            'city': 'street',
            'postal': {
                'numbers': '1245',
                'suffix': 'AB'
            }
        }
    }
    x = ObjectFiller(User).fill(json)    
    assert x.address != None
    assert x.address.city == 'street'
    
def test_inner_validation_missing_class_annotation():    
    class Adress:
        street: str
        city: str
    

    class User:
        address: Adress
    
    json = {
        'address': {
            'street': 'city',
            'city': 'street',
            'postal': {
                'numbers': '1245',
                'suffix': 'AB'
            }
        }
    }
    
    with raises(Exception) as e:
        ObjectFiller(User).fill(json)    
    
    assert str(e.value) == "Attribute 'postal' not found in class"
