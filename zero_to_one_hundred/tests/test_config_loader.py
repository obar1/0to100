"""Unit tests."""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401

from configs.config_loader import ConfigLoader


def test_load_yaml_config(map_config_file_path):
    config = ConfigLoader(map_config_file_path).load()
    assert config is not None
