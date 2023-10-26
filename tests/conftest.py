from pytest import fixture
from confclass.constants import ROOTDIR

@fixture
def testdir():
    return ROOTDIR / 'tests'