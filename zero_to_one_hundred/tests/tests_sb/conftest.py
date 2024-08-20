# pylint: disable=W0621,W0613
import os
from unittest import mock

import pytest

from zero_to_one_hundred.configs.a_config_map import AConfigMap
from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.factories.sb_factory import SBFactory
from zero_to_one_hundred.factories.sb_factory_provider import SBFactoryProvider
from zero_to_one_hundred.repository.sb_persist_fs import SBPersistFS
from zero_to_one_hundred.repository.sb_process_fs import SBProcessFS


@pytest.fixture
def persist_fs():
    yield SBPersistFS()


@pytest.fixture
def process_fs():
    yield SBProcessFS()


@pytest.fixture
def http_oreilly_1():
    yield "https://learning.oreilly.com/library/view/the-pragmatic-programmer/9780135956977/"


@pytest.fixture
def oreilly_isbn_1():
    yield "9780135956977"


@pytest.fixture
def http_oreilly_2():
    yield "https://learning.oreilly.com/library/view/clean-code-in/9781800560215/"


@pytest.fixture
def pages_tot():
    yield 999


@pytest.fixture
def page_curr():
    yield 99


get_resource_path = os.path.dirname(os.path.abspath(__file__)) + r"/resources"


@pytest.fixture
def get_map_yaml_path():
    yield get_resource_path + "/map.yaml"


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
def env_map_yaml(get_map_yaml_path):
    with mock.patch.dict(os.environ, {AConfigMap.MAP_YAML_PATH: get_map_yaml_path}):
        yield


@pytest.fixture
def get_config_map(env_map_yaml, get_map_yaml_path, persist_fs):
    return SBConfigMap(persist_fs)


@pytest.fixture
def get_factory_provider(persist_fs, process_fs):
    return SBFactoryProvider(persist_fs, process_fs)


@pytest.fixture
def get_factory(env_map_yaml, persist_fs, process_fs):
    return SBFactory(env_map_yaml, persist_fs, process_fs)
