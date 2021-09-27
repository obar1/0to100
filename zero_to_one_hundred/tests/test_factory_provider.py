# pylint: disable=C0116,R0903,E0401,W0703,W1201,redefined-outer-section,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203,W0613
import pytest

from factories.factory_provider import FactoryProvider
from factories.ztoh_factory import ZTOHFactory
from tests.moke.persist_fs import PersistFS as persist_fs


@pytest.fixture
def get_factory_provider(mock_settings_env_vars):
    return FactoryProvider(persist_fs)


def test_provide__pass(get_factory_provider):
    actual = get_factory_provider.provide()
    assert isinstance(actual, ZTOHFactory)


@pytest.fixture
def get_unsupported_factory_provider(mock_unsupported_map_yaml_env_vars):
    return FactoryProvider(persist_fs)


def test_provide__unsupported(get_unsupported_factory_provider):
    with pytest.raises(NotImplementedError):
        get_unsupported_factory_provider.provide()
