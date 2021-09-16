import pytest

from configs.config import ConfigMap
from factories.ztoh_factory import ZTOHFactory
from processors.create_section_processor import CreateSectionProcessor
from processors.refresh_sections_processor import RefreshSectionsProcessor
from tests.conftest import TestPersistFS

@pytest.fixture
def get_config_map(get_map_yaml_path):
    return ConfigMap(get_map_yaml_path, TestPersistFS.load_file)

@pytest.fixture
def get_args_get_processor():
    return  ["something"]

def test_get_processor(get_config_map,get_args_get_processor):
    actual = ZTOHFactory(get_config_map, TestPersistFS)
    with pytest.raises(ValueError):
        actual.get_processor(get_args_get_processor)

def test_section_processor(get_config_map,get_args_create_section_processor):
    actual = ZTOHFactory(get_config_map, TestPersistFS).get_processor(get_args_create_section_processor)
    assert isinstance(actual,CreateSectionProcessor)

def test_refresh_sections_processor(get_config_map,get_args_refresh_sections_processor):
    actual :RefreshSectionsProcessor= ZTOHFactory(get_config_map, TestPersistFS).get_processor(get_args_refresh_sections_processor)
    assert isinstance(actual,RefreshSectionsProcessor)
