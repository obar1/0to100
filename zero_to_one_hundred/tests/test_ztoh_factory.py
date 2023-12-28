import pytest

from zero_to_one_hundred.configs.config_map import ConfigMap
from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.repository.persist_fs import PersistFS as persist_fs
from zero_to_one_hundred.repository.process_fs import ProcessFS as process_fs


# pylint: disable=W0621


@pytest.fixture
def get_config_map(get_map_yaml_path):
    return ConfigMap(persist_fs, get_map_yaml_path)


def test_get_processor(get_config_map):
    ZTOHFactory(get_config_map, persist_fs, process_fs)


def test_N_processor():
    assert len(ZTOHFactory.SUPPORTED_PROCESSOR) == 5
