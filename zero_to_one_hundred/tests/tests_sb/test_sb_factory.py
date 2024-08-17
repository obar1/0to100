from zero_to_one_hundred.factories.sb_factory import SBFactory


# pylint: disable=W0621


def test_get_processor(get_config_map, persist_fs, process_fs):
    SBFactory(get_config_map, persist_fs, process_fs)


def test_N_processor():
    assert len(SBFactory.SUPPORTED_PROCESSOR) == 3
