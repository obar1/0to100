import pytest

from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.factories.ztoh_factory_provider import ZTOHFactoryProvider
from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS
from zero_to_one_hundred.repository.ztoh_process_fs import ZTOHProcessFS


# pylint: disable=W0621,W0613


def test_pass(get_config_map):
    actual = ZTOHFactoryProvider(ZTOHPersistFS, ZTOHProcessFS)
    assert isinstance(actual.provide(), ZTOHFactory)


def test_provide__unsupported(get_unsupported_factory_provider):
    with pytest.raises(NotImplementedError):
        get_unsupported_factory_provider.provide()
