"""Conftest module."""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401
import logging
import os
from typing import List
from unittest import mock

import pytest
import yaml

from factories.factory_provider import CONFIG_FILE

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)

# @pytest.fixture(scope="session", autouse=True)
# def callattr_ahead_of_alltests(get_resource_path, mock_settings_env_vars):
#     logging.info ('run_pre_start')
#     yield
#     logging.info ('run_after_finish')


@pytest.fixture
def wip():
    logging.info("~"*88)

@pytest.fixture
def http_url():
    yield "https://cloud.google.com/docs"

@pytest.fixture
def get_test_path():
    os_path_dirname = os.path.dirname(os.path.abspath(__file__))
    logging.debug(os_path_dirname)
    return os_path_dirname

@pytest.fixture
def get_version(get_test_path):
    return get_test_path + "/../../version"

@pytest.fixture
def get_resource_path(get_test_path):
    return get_test_path + '/resources'

@pytest.fixture
def get_map_yaml_path(get_resource_path):
    yield get_resource_path + '/map.yaml'

@pytest.fixture
def get_unsupported_map_yaml_path(get_resource_path):
    yield get_resource_path + '/unsupported_map.yaml'

@pytest.fixture
def mock_settings_env_vars(get_map_yaml_path):
    with mock.patch.dict(os.environ, {CONFIG_FILE: get_map_yaml_path}):
        yield

@pytest.fixture
def mock_unsupported_map_yaml_env_vars(get_unsupported_map_yaml_path):
    with mock.patch.dict(os.environ, {CONFIG_FILE: get_unsupported_map_yaml_path}):
        yield

@pytest.fixture
def get_create_section_params()->List[str]:
    return ["main.py","create_section","https://cloud.google.com/docs"]

@pytest.fixture
def get_refresh_sections_params() -> List[str]:
    return ["main.py","refresh_sections", ""]



class TestPersistFS:
    @classmethod
    def write_section(cls, section):
        return "write_section_MOCK"

    @classmethod
    def refresh_sections(cls,map):
        return "refresh_map_MOCK"

    @classmethod
    def load_file(cls,config_file):
        with open(config_file, "r") as stream:
            return yaml.safe_load(stream)
    # TOOD: use hard code


    @classmethod
    def write_file(cls, readme_md, txt):
        return True


