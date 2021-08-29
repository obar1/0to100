"""Unit tests."""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401

from configs.config import Config


def test_load_yaml_config(get_root, config_loader: Config):
    assert config_loader.get_config_type() == "map"
    assert config_loader.get_repo_path() == get_root + "/resources" + "/map.md"
    assert config_loader.get_repo_sorted() is True
