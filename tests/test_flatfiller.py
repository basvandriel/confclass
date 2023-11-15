from configurationclass.filler.flat_object_filler import ObjectFiller


def test_flatfiller():
    class User:
        name: str
        age: int
        
    filler = ObjectFiller(User)
    x = filler.fill({
        "name": 'Bas',
        'age': 23
    })
    assert x.age == 23