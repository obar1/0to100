import pytest

from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.factories.ztoh_factory_provider import ZTOHFactoryProvider


# pylint: disable=W0621,W0613


def test_pass(get_config_map, persist_fs, process_fs):
    actual = ZTOHFactoryProvider(persist_fs, process_fs)
    assert isinstance(actual.provide(), ZTOHFactory)


def test_provide__unsupported(env_unsupported_map_yaml, persist_fs, process_fs):
    with pytest.raises(NotImplementedError):
        ZTOHFactoryProvider(persist_fs, process_fs).provide()
