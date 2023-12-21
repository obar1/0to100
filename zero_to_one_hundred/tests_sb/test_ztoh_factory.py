import pytest

from zero_to_one_hundred.configs.config_map import ConfigMap
from zero_to_one_hundred.factories.sb_factory import SBFactory
from zero_to_one_hundred.tests.moke import persist_fs_fake, process_fs_fake

# pylint: disable=W0621


@pytest.fixture
def get_config_map(get_map_yaml_path):
    return ConfigMap(persist_fs_fake, get_map_yaml_path)


def test_get_processor(get_config_map):
    SBFactory(persist_fs_fake, process_fs_fake, get_config_map)


def test_N_processor():
    assert len(SBFactory.SUPPORTED_PROCESSOR) == 3
