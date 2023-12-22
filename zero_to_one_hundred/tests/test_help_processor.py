from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.processors.help_processor import HelpProcessor
from zero_to_one_hundred.tests.moke import persist_fs_fake, process_fs_fake


def test_process(get_config_map):
    actual: HelpProcessor = ZTOHFactory(
        persist_fs_fake, process_fs_fake, get_config_map
    ).get_processor([None, "help"])
    for p in actual:
        assert p.process() is None
