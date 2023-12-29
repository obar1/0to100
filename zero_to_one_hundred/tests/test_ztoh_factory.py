from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS as persist_fs
from zero_to_one_hundred.repository.ztoh_process_fs import ZTOHProcessFS as process_fs

# pylint: disable=W0621


def test_get_processor(get_config_map):
    ZTOHFactory(get_config_map, persist_fs, process_fs)


def test_N_processor():
    assert len(ZTOHFactory.SUPPORTED_PROCESSOR) == 5
