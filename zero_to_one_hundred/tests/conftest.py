# pylint: disable=W0621,W0613

import os
import string
from unittest import mock

import pytest

from zero_to_one_hundred.configs.a_config_map import AConfigMap
from zero_to_one_hundred.configs.ztoh_config_map import ZTOHConfigMap
from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.factories.ztoh_factory_provider import ZTOHFactoryProvider
from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS
from zero_to_one_hundred.tests.repository.ztoh_process_fs import ZTOHProcessFS


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
def get_map_yaml_path(get_resource_path):
    yield get_resource_path + "/map.yaml"


@pytest.fixture
def get_unsupported_map_yaml_path(get_resource_path):
    yield get_resource_path + "/unsupported_map.yaml"


@pytest.fixture
def get_gcp_map_yaml_path(get_resource_path):
    yield get_resource_path + "/gcp_map.yaml"


@pytest.fixture
def get_datacamp_map_yaml_path(get_resource_path):
    yield get_resource_path + "/datacamp_map.yaml"


@pytest.fixture
def get_sample_readme_md_path(get_repo_path):
    yield get_repo_path + "/https§§§cloud.google.com§docs/readme.md"


@pytest.fixture
def env_map_yaml(get_map_yaml_path):
    with mock.patch.dict(os.environ, {AConfigMap.MAP_YAML_PATH: get_map_yaml_path}):
        yield


@pytest.fixture
def env_unsupported_map_yaml(get_unsupported_map_yaml_path):
    with mock.patch.dict(
        os.environ, {AConfigMap.MAP_YAML_PATH: get_unsupported_map_yaml_path}
    ):
        yield


@pytest.fixture
def env_gcp_map_yaml(get_gcp_map_yaml_path):
    with mock.patch.dict(os.environ, {AConfigMap.MAP_YAML_PATH: get_gcp_map_yaml_path}):
        yield


@pytest.fixture
def env_datacamp_map_yaml(get_datacamp_map_yaml_path):
    with mock.patch.dict(
        os.environ, {AConfigMap.MAP_YAML_PATH: get_datacamp_map_yaml_path}
    ):
        yield


@pytest.fixture
def persist_fs():
    yield ZTOHPersistFS()


@pytest.fixture
def process_fs():
    yield ZTOHProcessFS()


@pytest.fixture
def get_config_map(env_map_yaml, get_map_yaml_path, persist_fs):
    return ZTOHConfigMap(persist_fs)


@pytest.fixture
def get_unsupported_config_map(
    env_unsupported_map_yaml, get_unsupported_map_yaml_path, persist_fs
):
    return ZTOHConfigMap(persist_fs)


@pytest.fixture
def get_gcp_config_map(env_gcp_map_yaml, get_gcp_map_yaml_path, persist_fs):
    return ZTOHConfigMap(persist_fs)


@pytest.fixture
def get_datacamp_config_map(
    env_datacamp_map_yaml, get_datacamp_map_yaml_path, persist_fs
):
    return ZTOHConfigMap(persist_fs)


@pytest.fixture
def get_factory(env_map_yaml, persist_fs, process_fs):
    return ZTOHFactory(get_config_map, persist_fs, process_fs)


@pytest.fixture
def get_factory_provider(env_map_yaml, persist_fs, process_fs):
    return ZTOHFactoryProvider(persist_fs, process_fs)


@pytest.fixture
def simple_http():
    return "https://cloud.google.com/docs/<>:?*"


@pytest.fixture
def simple_dir():
    return "https§§§cloud.google.com§docs§§§§§§"


@pytest.fixture
def dir_tree():
    return "https§§§cloud.google.com§sections"


def str_relaxed(s1):
    remove = string.whitespace
    mapping = {ord(c): None for c in remove}
    return s1.translate(mapping)
