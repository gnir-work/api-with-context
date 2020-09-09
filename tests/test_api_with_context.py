import pytest
from api_with_context import __version__
from api_with_context.api import awesome_api
from api_with_context.context import Context


@pytest.fixture
def test_context():
    return Context('some id', 'awesome folder')


def test_version():
    assert __version__ == '0.1.0'


def test_initialization(test_context):
    # Initialization
    assert awesome_api._context is None
    awesome_api.load_context(test_context)

    # Usage of api
    assert awesome_api.id == test_context.id
    assert awesome_api.folder == test_context.folder
