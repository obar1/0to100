from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory

# pylint: disable=W0621


def test_get_processor(get_config_map, persist_fs, process_fs):
    ZTOHFactory(get_config_map, persist_fs, process_fs)


def test_N_processor():
    assert len(ZTOHFactory.SUPPORTED_PROCESSOR) == 5
