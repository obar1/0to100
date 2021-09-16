from factories.ztoh_factory import ZTOHFactory
from processors.create_section_processor import CreateSectionProcessor
from tests.conftest import TestPersistFS


def test_process(get_config_map, get_args_create_section_processor):
    actual: CreateSectionProcessor = ZTOHFactory(get_config_map, TestPersistFS).get_processor(
        get_args_create_section_processor)
    actual.process()

