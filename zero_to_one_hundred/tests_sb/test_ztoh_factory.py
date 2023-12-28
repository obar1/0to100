from zero_to_one_hundred.factories.sb_factory import SBFactory
from zero_to_one_hundred.repository.persist_fs import PersistFS as persist_fs
from zero_to_one_hundred.repository.process_fs import ProcessFS as process_fs


# pylint: disable=W0621


def test_get_processor(get_config_map):
    SBFactory(persist_fs, process_fs, get_config_map)


def test_N_processor():
    assert len(SBFactory.SUPPORTED_PROCESSOR) == 4
