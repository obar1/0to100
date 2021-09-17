from factories.ztoh_factory import ZTOHFactory
from processors.refresh_sections_processor import RefreshSectionsProcessor
from tests.moke.persist_fs import PersistFS


def test_process(get_config_map, get_args_create_section_processor):
    actual: RefreshSectionsProcessor = ZTOHFactory(get_config_map, PersistFS).get_processor(
        get_args_create_section_processor)
    actual.process()

