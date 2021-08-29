"""Conftest module."""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401
import logging
import os

import pytest

from configs.config_loader import ConfigLoader
from factories.factory_provider import FactoryProvider

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)


@pytest.fixture(scope="session", autouse=True)
def get_root():
    return os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope="session", autouse=True)
def map_config_file_path(get_root):
    return get_root + "/resources/map_config.yaml"


@pytest.fixture(scope="session", autouse=True)
def get_version(get_root):
    return get_root + "/../../version"


@pytest.fixture(scope="session", autouse=True)
def get_map_md(get_root):
    return get_root + "/resources/map.md"


@pytest.fixture
def config_loader(map_config_file_path):
    return ConfigLoader(map_config_file_path).load()


@pytest.fixture
def run_section(args):
    factory = FactoryProvider(args).provide()
    return factory.create_section_processor().process()
