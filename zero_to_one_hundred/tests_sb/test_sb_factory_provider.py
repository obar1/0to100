from zero_to_one_hundred.factories.sb_factory import SBFactory

from zero_to_one_hundred.factories.sb_factory_provider import SBFactoryProvider
from zero_to_one_hundred.repository.sb_persist_fs import SBPersistFS
from zero_to_one_hundred.repository.sb_process_fs import SBProcessFS


# pylint: disable=W0621


def test_pass(get_config_map):
    actual = SBFactoryProvider(SBPersistFS, SBProcessFS)
    assert isinstance(actual.provide(), SBFactory)
