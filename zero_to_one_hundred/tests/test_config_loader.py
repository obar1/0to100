"""Unit tests."""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401
from testfixtures import TempDirectory

from configs.config_loader import ConfigLoader

def test_load_yaml_config(get__tmp__map_config__file_path):
    config = ConfigLoader(get__tmp__map_config__file_path).load()
    assert config is not None
