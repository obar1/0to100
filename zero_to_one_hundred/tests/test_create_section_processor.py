from factories.ztoh_factory import ZTOHFactory
from processors.create_section_processor import CreateSectionProcessor
from tests.moke.persist_fs import PersistFS


def test_process(get_config_map, get_args_create_section_processor):
    actual: CreateSectionProcessor = ZTOHFactory(get_config_map, PersistFS).get_processor(
        get_args_create_section_processor)
    actual.process()
