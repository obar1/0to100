import pytest

from factories.factory_provider import  FactoryProvider
from factories.ztoh_factory import ZTOHFactory
from tests.conftest import TestPersistFS


@pytest.fixture
def get_factory_provider(mock_settings_env_vars):
    return FactoryProvider(TestPersistFS)

def test_provide__pass(get_factory_provider):
    actual = get_factory_provider.provide()
    assert isinstance(actual,ZTOHFactory)

@pytest.fixture
def get_unsupported_factory_provider(mock_unsupported_map_yaml_env_vars):
    return FactoryProvider(TestPersistFS)

def test_provide__unsupported(get_unsupported_factory_provider):
    with pytest.raises(NotImplementedError):
        get_unsupported_factory_provider.provide()
