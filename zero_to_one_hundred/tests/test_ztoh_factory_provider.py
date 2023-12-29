import pytest

from zero_to_one_hundred.configs.ztoh_config_map import ZTOHConfigMap
from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.factories.ztoh_factory_provider import ZTOHFactoryProvider
from zero_to_one_hundred.repository.persist_fs import PersistFS
from zero_to_one_hundred.repository.process_fs import ProcessFS


# pylint: disable=W0621


def test_pass(get_config_map):
    actual = ZTOHFactoryProvider(PersistFS, ProcessFS)
    assert isinstance(actual.provide(), ZTOHFactory)


def test_provide__unsupported(get_unsupported_factory_provider):
    with pytest.raises(NotImplementedError):
        get_unsupported_factory_provider.provide()
