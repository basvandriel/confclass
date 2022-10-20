# import confclass

from dataclasses import dataclass
from confclass import confclass

from pytest import raises

def test_decorator_on_func():
    with raises(ValueError) as excinfo:
        @confclass()
        def _():
            ...
            
    assert str(excinfo.value) == 'Decorator can only be used on a class'

def test_decorator_no_args():
    with raises(ValueError) as excinfo:
        @confclass
        class _:
            ...
            
    assert str(excinfo.value) == 'Decorator can only be used with parameters'
    