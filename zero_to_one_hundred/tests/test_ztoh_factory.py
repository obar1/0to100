import pytest

from zero_to_one_hundred.configs.config_map import ConfigMap
from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.tests.moke.persist_fs_fake import (
    PersistFSFake as persist_fs_fake,
)
from zero_to_one_hundred.tests.moke.process_fs_fake import (
    ProcessFSFake as process_fs_fake,
)

# pylint: disable=W0621


@pytest.fixture
def get_config_map(get_map_yaml_path):
    return ConfigMap(persist_fs_fake, get_map_yaml_path)


def test_get_processor(get_config_map):
    ZTOHFactory(persist_fs_fake, process_fs_fake, get_config_map)


def test_N_processor():
    assert len(ZTOHFactory.SUPPORTED_PROCESSOR) == 5
