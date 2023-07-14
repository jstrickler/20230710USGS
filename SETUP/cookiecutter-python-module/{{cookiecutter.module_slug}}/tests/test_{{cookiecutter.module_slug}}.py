import pytest
from {{cookiecutter.module_slug}} import {{cookiecutter.module_slug | title}}, sample_function

@pytest.fixture
def {{cookiecutter.module_slug | title}}_object():
    obj = {{cookiecutter.module_slug | title}}()
    return obj

def test_{{cookiecutter.module_slug | title}}_instance_has_sample_method({{cookiecutter.module_slug | title}}_object):
    assert hasattr({{cookiecutter.module_slug | title}}_object, "sample_method")

def test_{{cookiecutter.module_slug}}_has_sample_function():
    assert sample_function() is None  # no return value
