from src.zero_to_one_hundred.factories.ztoh_factory import (
    ZTOHFactory,
)

# pylint: disable=W0621


def test_get_processor(get_config_map, persist_fs):
    ZTOHFactory(get_config_map, persist_fs)


def test_N_processor():
    # PDF to MD processor was added, update expected count
    assert len(ZTOHFactory.SUPPORTED_PROCESSOR) == 6
