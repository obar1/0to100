# pylint: disable=W0621,W0613

import os
from unittest import mock

import pytest

from src.zero_to_one_hundred.configs.a_config_map import AConfigMap
from src.zero_to_one_hundred.configs.ztoh_config_map import (
    ZTOHConfigMap,
)
from src.zero_to_one_hundred.factories.ztoh_factory import (
    ZTOHFactory,
)
from src.zero_to_one_hundred.factories.ztoh_factory_provider import (
    ZTOHFactoryProvider,
)
from src.zero_to_one_hundred.repository.ztoh_persist_fs import (
    ZTOHPersistFS,
)

get_resource_path = os.path.dirname(os.path.abspath(__file__)) + r"/resources"


@pytest.fixture(scope="session")
def persist_fs():
    yield ZTOHPersistFS()


@pytest.fixture
def get_map_yaml_path():
    yield get_resource_path + "/map.yaml"


@pytest.fixture
def get_map_sorted_0_yaml_path():
    yield get_resource_path + "/map_sorted_0.yaml"


@pytest.fixture
def get_map_sorted_1_yaml_path():
    yield get_resource_path + "/map_sorted_1.yaml"


@pytest.fixture
def get_unsupported_map_yaml_path():
    yield get_resource_path + "/unsupported_map.yaml"


@pytest.fixture
def get_sample_readme_md_path(get_repo_path):
    yield get_repo_path + "/https§§§cloud.google.com§docs/readme.md"


@pytest.fixture
def env_map_sorted_0_yaml(get_map_sorted_0_yaml_path):
    with mock.patch.dict(
        os.environ, {AConfigMap.MAP_YAML_PATH: get_map_sorted_0_yaml_path}
    ):
        yield


@pytest.fixture
def env_map_sorted_1_yaml(get_map_sorted_1_yaml_path):
    with mock.patch.dict(
        os.environ, {AConfigMap.MAP_YAML_PATH: get_map_sorted_1_yaml_path}
    ):
        yield


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
def get_config_map(env_map_yaml, get_map_yaml_path, persist_fs):
    return ZTOHConfigMap(persist_fs)


@pytest.fixture
def get_config_map_sorted_0(
    env_map_sorted_0_yaml, get_map_sorted_0_yaml_path, persist_fs
):
    return ZTOHConfigMap(persist_fs)


@pytest.fixture
def get_config_map_sorted_1(
    env_map_sorted_1_yaml, get_map_sorted_1_yaml_path, persist_fs
):
    return ZTOHConfigMap(persist_fs)


@pytest.fixture
def get_unsupported_config_map(
    env_unsupported_map_yaml, get_unsupported_map_yaml_path, persist_fs
):
    return ZTOHConfigMap(persist_fs)


@pytest.fixture
def get_factory(env_map_yaml, persist_fs):
    return ZTOHFactory(env_map_yaml, persist_fs)


@pytest.fixture
def get_factory_provider(env_map_yaml, persist_fs):
    return ZTOHFactoryProvider(persist_fs)


@pytest.fixture
def fs():
    patcher = Patcher()
    patcher.setUp()
    yield patcher.fs  # Provide the fake filesystem
    patcher.tearDown()
