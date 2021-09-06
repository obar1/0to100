"""Conftest module."""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401
import logging
import os
from unittest import mock

import pytest
from testfixtures import TempDirectory
from typing import List

from configs.config import Config
from configs.config_loader import ConfigLoader
from factories.factory_provider import FactoryProvider, CONFIG_FILE

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)

# @pytest.fixture(scope="session", autouse=True)
# def get_local_home():
#     tc =TempDirectory()
#     logging.info(tc.path)
#     yield tc
#
#



@pytest.fixture
def wip():
    logging.info("~"*88)

@pytest.fixture(scope="session", autouse=True)
def get_repo_root():
    return os.path.dirname(os.path.abspath(__file__))

@pytest.fixture(scope="session", autouse=True)
def get_local_home(get_repo_root):
    return  get_repo_root+ '/local'


@pytest.fixture(scope="session", autouse=True)
def get_version(get_repo_root):
    return get_repo_root + "/../../version"


@pytest.fixture(scope="session", autouse=True)
def get__tmp__map_config__file_path(get_repo_root, get_local_home):
    from shutil import copyfile
    config_yaml_ = get_local_home + '/map_config.yaml'
    copyfile(get_repo_root + "/resources/map_config.yaml", config_yaml_)
    return config_yaml_


@pytest.fixture
def config_loader(get__tmp__map_config__file_path)->Config:
    return ConfigLoader(get__tmp__map_config__file_path).load()


@pytest.fixture(scope="session", autouse=True)
def get__tmp__map_md__file_path(get_repo_root, get_local_home):
    from shutil import copyfile
    map_md_ = get_local_home + '/map.md'
    copyfile(get_repo_root + "/resources/map.md", map_md_)
    return map_md_

@pytest.fixture(scope="session", autouse=True)
def mock_settings_env_vars(get_local_home, get__tmp__map_config__file_path, get__tmp__map_md__file_path):
    with mock.patch.dict(os.environ, {CONFIG_FILE: get__tmp__map_config__file_path}):
        yield


@pytest.fixture(scope="session", autouse=True)
def callattr_ahead_of_alltests(get_local_home, mock_settings_env_vars):
    logging.info ('run_pre_start')
    yield
    logging.info ('run_after_finish')


@pytest.fixture
def get_create_section_params()->List[str]:
    return ["main.py","create_section","https://cloud.google.com/docs"]


@pytest.fixture
def get_refresh_sections_params() -> List[str]:
    return ["main.py","refresh_sections", ""]