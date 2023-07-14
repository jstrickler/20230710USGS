import pytest
from mycoolmodule import Mycoolmodule, sample_function

@pytest.fixture
def Mycoolmodule_object():
    obj = Mycoolmodule()
    return obj

def test_Mycoolmodule_instance_has_sample_method(Mycoolmodule_object):
    assert hasattr(Mycoolmodule_object, "sample_method")

def test_mycoolmodule_has_sample_function():
    assert sample_function() is None  # no return value
