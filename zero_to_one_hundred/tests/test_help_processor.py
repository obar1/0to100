from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.processors.help_processor import HelpProcessor
from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS as persist_fs
from zero_to_one_hundred.repository.ztoh_process_fs import ZTOHProcessFS as process_fs


def test_process(get_config_map):
    actual: HelpProcessor = ZTOHFactory(
        get_config_map, persist_fs, process_fs
    ).get_processor([None, "help"])
    for p in actual:
        p.process()
