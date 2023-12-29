# pylint: disable=W0621,W0613

import os
from unittest import mock

import pytest

from zero_to_one_hundred.configs.a_config_map import AConfigMap
from zero_to_one_hundred.configs.ztoh_config_map import ZTOHConfigMap
from zero_to_one_hundred.factories.ztoh_factory_provider import ZTOHFactoryProvider
from zero_to_one_hundred.repository.persist_fs import PersistFS
from zero_to_one_hundred.repository.process_fs import ProcessFS


@pytest.fixture
def http_url():
    yield "https://cloud.google.com/abc"


@pytest.fixture
def http_url_2():
    yield "https://cloud.google.com/zzz"


@pytest.fixture
def http_url_3():
    yield "https://cloud.google.com/zzz/123"


@pytest.fixture
def http_url_4():
    yield "https://cloudskillsboost.google/"


@pytest.fixture
def get_test_path():
    os_path_dirname = os.path.dirname(os.path.abspath(__file__))
    yield os_path_dirname


@pytest.fixture
def get_resource_path(get_test_path):
    yield get_test_path + "/resources"


@pytest.fixture
def get_repo_path(get_resource_path):
    yield get_resource_path + "/repo"


@pytest.fixture
def get_map_yaml_path(get_resource_path):
    yield get_resource_path + "/map.yaml"


@pytest.fixture
def get_unsupported_map_yaml_path(get_resource_path):
    yield get_resource_path + "/unsupported_map.yaml"


@pytest.fixture
def get_sample_readme_md_path(get_repo_path):
    yield get_repo_path + "/https§§§cloud.google.com§docs/readme.md"


@pytest.fixture
def mock_settings_env_vars(get_map_yaml_path):
    with mock.patch.dict(os.environ, {AConfigMap.MAP_YAML_PATH: get_map_yaml_path}):
        yield


@pytest.fixture
def mock_unsupported_map_yaml_env_vars(get_unsupported_map_yaml_path):
    with mock.patch.dict(
        os.environ, {AConfigMap.MAP_YAML_PATH: get_unsupported_map_yaml_path}
    ):
        yield


@pytest.fixture
def get_unsupported_factory_provider(mock_unsupported_map_yaml_env_vars):
    return ZTOHFactoryProvider(PersistFS, ProcessFS)


@pytest.fixture
def get_config_map(mock_settings_env_vars, get_map_yaml_path):
    return ZTOHConfigMap(PersistFS)


@pytest.fixture
def get_factory_provider(mock_settings_env_vars):
    return ZTOHFactoryProvider(PersistFS, ProcessFS)


@pytest.fixture
def simple_http():
    return "https://cloud.google.com/docs/<>:?*"


@pytest.fixture
def simple_dir():
    return "https§§§cloud.google.com§docs§§§§§§"


@pytest.fixture
def dir_tree():
    return "https§§§cloud.google.com§sections"
