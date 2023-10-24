from inspect import isclass


# def confclass(cls: object | None = None):
#     # When confclass is called without "()" (@confclass), an error should appear
#     # In that case, cls is filled in. Also, funcs aren't allowed
#     if cls is None:
#         raise ValueError("Decorator can only be used with parameters")
#     if not isclass(cls):
#         raise ValueError("Decorator can only be used on a class")

#     def wrap(cls):
#         return ClassProcessor().process(cls)

#     return wrap
