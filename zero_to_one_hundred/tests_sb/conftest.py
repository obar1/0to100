"""Conftest module."""


import os
from unittest import mock

import pytest

SAFARI_BOOKS = "safari-books"
MAP_YAML_PATH = "MAP_YAML_PATH"
RUNME = "RUNME"


@pytest.fixture
def http_url():
    yield "https://learning.oreilly.com/library/view/the-pragmatic-programmer/9780135956977/"


@pytest.fixture
def http_url_isbn():
    yield "9780135956977"


@pytest.fixture
def http_url_2():
    yield "https://www.oreilly.com/library/view/data-pipelines-pocket/9781492087823/"


@pytest.fixture
def dir_name():
    return "https:§§cloud.google.com§docs"


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
def get_secret_map_yaml_path(get_resource_path):
    yield get_resource_path + "/secret_map.yaml"


@pytest.fixture
def mock_map_yaml_env_vars(get_map_yaml_path):
    with mock.patch.dict(os.environ, {MAP_YAML_PATH: get_map_yaml_path}):
        yield


@pytest.fixture
def mock_secret_map_yaml_env_vars(get_secret_map_yaml_path):
    with mock.patch.dict(os.environ, {MAP_YAML_PATH: get_secret_map_yaml_path}):
        yield


@pytest.fixture
def get_args_create_meta_book_processor():
    return [RUNME, "create_meta_book"]


@pytest.fixture
def get_args_refresh_toc_processor():
    return [RUNME, "refresh_toc"]


@pytest.fixture
def get_args_help_processor():
    return [RUNME, "help"]


@pytest.fixture
def get_args_unsupported_processor():
    return [RUNME, "something"]
