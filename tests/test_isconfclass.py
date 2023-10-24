from confclass.main import Configuration, confclass, is_confclass, get_configuration

def test_class_annotation():
    @confclass
    class T:
        haha: str
        
    object = T()
    
    class Z:
        ...
    
    assert is_confclass(object)
    assert not is_confclass(Z()) 
    
    
def test_inheritence():
    # I don't think it's a good idea to actually have it magically inhererit.
    # why not make some abstract factory thing?
    @confclass
    class T:
        haha: str
    
    conf: Configuration = get_configuration(T())
    assert isinstance(conf, Configuration)