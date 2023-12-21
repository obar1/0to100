# pylint: disable=W0621,W0613

import os
from unittest import mock

import pytest

from zero_to_one_hundred.configs.a_config_map import AConfigMap
from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.tests_sb.moke.sb_persist_fs_fake import (
    SBPersistFSFake as persist_fs_fake,
)


@pytest.fixture
def http_url():
    yield "https://learning.oreilly.com/library/view/the-pragmatic-programmer/9780135956977/"


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
def mock_map_yaml_env_vars(get_map_yaml_path):
    with mock.patch.dict(os.environ, {AConfigMap.MAP_YAML_PATH: get_map_yaml_path}):
        yield


@pytest.fixture
def mock_secret_map_yaml_env_vars(get_secret_map_yaml_path):
    with mock.patch.dict(
        os.environ, {AConfigMap.MAP_YAML_PATH: get_secret_map_yaml_path}
    ):
        yield


@pytest.fixture
def mock_settings_env_vars(get_map_yaml_path):
    with mock.patch.dict(os.environ, {AConfigMap.MAP_YAML_PATH: get_map_yaml_path}):
        yield


@pytest.fixture
def get_config_map(get_map_yaml_path):
    return SBConfigMap(get_map_yaml_path, persist_fs_fake)
