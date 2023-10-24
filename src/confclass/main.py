def confclass(cls: object):
    cls.CONFCLASS_NAME = 'confclass'
    return cls

def is_confclass(obj: object) -> bool:
    return hasattr(obj, 'CONFCLASS_NAME')