# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import pytest

from configs.config import ConfigMap
from factories.ztoh_factory import ZTOHFactory
from tests.moke.persist_fs import PersistFS as persist_fs


@pytest.fixture
def get_config_map(get_map_yaml_path):
    return ConfigMap(get_map_yaml_path, persist_fs)


@pytest.fixture
def get_args_get_processor():
    return ["runme.sh", "something"]


def test_get_processor(get_config_map, get_args_get_processor):
    actual = ZTOHFactory(get_config_map, persist_fs)
    with pytest.raises(ValueError):
        actual.get_processor(get_args_get_processor)
