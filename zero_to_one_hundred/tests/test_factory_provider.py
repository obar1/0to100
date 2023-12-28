import pytest

from zero_to_one_hundred.factories.ztoh_factory_provider import ZTOHFactoryProvider
from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.repository.persist_fs import PersistFS as persist_fs
from zero_to_one_hundred.repository.process_fs import ProcessFS as process_fs


# pylint: disable=W0621,W0613


@pytest.fixture
def get_factory_provider(mock_settings_env_vars):
    return ZTOHFactoryProvider(persist_fs, process_fs)


def test_provide__pass(get_factory_provider):
    actual = get_factory_provider.provide()
    assert isinstance(actual, ZTOHFactory)


@pytest.fixture
def get_unsupported_factory_provider(mock_unsupported_map_yaml_env_vars):
    return ZTOHFactoryProvider(persist_fs, process_fs)


def test_provide__unsupported(get_unsupported_factory_provider):
    with pytest.raises(NotImplementedError):
        get_unsupported_factory_provider.provide()
