from confclass.main import confclass, is_confclass

def test_class_annotation():
    @confclass
    class T:
        haha: str
        
    object = T()
    
    class Z:
        ...
    
    assert is_confclass(object)
    assert not is_confclass(Z()) 