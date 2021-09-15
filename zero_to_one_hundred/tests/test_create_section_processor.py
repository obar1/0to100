import pytest

from configs.config import ConfigMap
from factories.ztoh_factory import ZTOHFactory
from processors.create_section_processor import CreateSectionProcessor
from repository.persist_fs import PersistFS


@pytest.fixture
def get_config_map(get_map_yaml_path):
    return ConfigMap(get_map_yaml_path, PersistFS.load_file)

def test_process(get_config_map,get_args_create_section_processor):
    actual:CreateSectionProcessor = ZTOHFactory(get_config_map, PersistFS).get_processor(get_args_create_section_processor)
    assert actual.process() is True