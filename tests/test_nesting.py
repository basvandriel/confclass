from confclass.object_filler import ObjectFiller


def test_1level_validation():
    class User:
        name: str
        age: int
    
    # TODO it should also fail when it's missing properties.
    # Currently, only functions when it has the attribute in the dict,
    # but not in the class annotations. Should be bi-directional.
    json = {
        'name': 'Bas',
    }
    x = ObjectFiller(User).fill(json)   
    print(x)
    
    
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
        name: str
        age: int
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
    
def test_2level_nest_validation():
    class Postal:
        numbers: str
        suffix: str
    
    class Adress:
        street: str
        city: str
        postal: Postal        

    class User:
        name: str
        age: int
        address: Adress
        
    json = {
        'address': {
            'street': 'city',
            'city': 'street',
            'postal': {
                # 'numbers': '1245',
                'suffix': 'AB'
            }
        }
    }
    x = ObjectFiller(User).fill(json)    
    assert x.address != None
    assert x.address.city == 'street'