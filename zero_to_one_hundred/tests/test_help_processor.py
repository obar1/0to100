from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.processors.help_processor import HelpProcessor


def test_process(
    get_config_map,
    persist_fs,
    process_fs,
):
    actual: HelpProcessor = ZTOHFactory(
        get_config_map,
        persist_fs,
        process_fs,
    ).get_processor([None, "help"])
    for p in actual:
        p.process()
