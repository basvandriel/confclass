from pytest import fixture
from pathlib import Path

ROOTDIR: Path = Path(__file__).parent.parent

@fixture
def testdir():
    return ROOTDIR / 'tests'