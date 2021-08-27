"""Conftest module."""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401

import os

import pytest

from configs.config_loader import ConfigLoader

ROOT = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope="session", autouse=True)
def map_config_file_path():
    """TODO."""
    return ROOT + "/resources/map_config.yaml"


@pytest.fixture
def config_loader(map_config_file_path):
    return ConfigLoader(map_config_file_path).load()
