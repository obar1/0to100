import pytest

from configs.config import Config, ConfigMap
from repository.persist_fs import PersistFS

@pytest.fixture
def get_persist_fs_load_file():
    return PersistFS.load_file

@pytest.fixture
def get_config(get_map_yaml_path, get_persist_fs_load_file):
    return Config(get_map_yaml_path, get_persist_fs_load_file)

def test_get_type(get_config):
    assert get_config.get_type == 'map'

@pytest.fixture
def get_config_map(get_map_yaml_path, get_persist_fs_load_file):
    return ConfigMap(get_map_yaml_path, get_persist_fs_load_file)

def test_get_repo_path(get_config_map, get_map_yaml_path):
    assert get_config_map.get_repo_path == './repo'

def test_get_map_md(get_config_map):
    assert get_config_map.get_repo_map_md == 'map.md'

def test_get_repo_sorted(get_config_map):
    assert get_config_map.get_repo_sorted is True

