from confclass.object_filler import ObjectFiller


class Adress:
    street: str
    city: str

class User:
    name: str
    age: int
    address: Adress
    
def test_testing():
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