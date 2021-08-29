"""Unit tests."""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401
import os

import pytest

from factories.factory_provider import CONFIG_FILE


def test_version(get_version):
    expected = "0.0.3"
    with open(get_version, mode="r", encoding="UTF-8") as file_handle:
        assert file_handle.read().lower().strip("\n") == expected


@pytest.fixture
def get_args(get_config_file, get_map_md):
    os.environ[CONFIG_FILE] = get_config_file
