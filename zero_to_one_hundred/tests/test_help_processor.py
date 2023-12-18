from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.processors.help_processor import HelpProcessor
from zero_to_one_hundred.repository.persist_fs import PersistFS as persist_fs
from zero_to_one_hundred.tests.moke.process_fs_fake import ProcessFSFake as process_fs


def test_process(
        get_config_map,
        get_args_help_processor,
):
    actual: HelpProcessor = ZTOHFactory(
        persist_fs, process_fs, get_config_map
    ).get_processor(get_args_help_processor)
    for p in actual:
        assert p.process() is None
