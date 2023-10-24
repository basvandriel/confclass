from typing import Self


class Configuration:
    def hi(self):
        print('hi')
    
def confclass(obj: object):
    obj.CONFCLASS_NAME = 'confclass'
    
    # T = obj.__class__
    # class K(Configuration, T):
    #     ...
    t: Configuration =  type(obj.__name__, (Configuration, obj), {})
    return t

def is_confclass(obj: object) -> bool:
    return hasattr(obj, 'CONFCLASS_NAME')


def get_configuration(confclass: object) -> Configuration | None:
    if not is_confclass(confclass) or not isinstance(confclass, Configuration):
        return None
    
    return confclass




