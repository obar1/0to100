# pylint: disable=C0116,R0903,E0401,W0703,W1201,redefined-outer-name,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103
import pytest

from configs.config import ConfigMap
from factories.ztoh_factory import ZTOHFactory
from processors.create_section_processor import CreateSectionProcessor
from processors.refresh_map_processor import RefreshMapProcessor
from tests.moke.persist_fs import PersistFS as persist_fs


@pytest.fixture
def get_config_map(get_map_yaml_path):
    return ConfigMap(get_map_yaml_path, persist_fs)


@pytest.fixture
def get_args_get_processor():
    return ["something"]


def test_get_processor(get_config_map, get_args_get_processor):
    actual = ZTOHFactory(get_config_map, persist_fs)
    with pytest.raises(ValueError):
        actual.get_processor(get_args_get_processor)


def test_section_processor(get_config_map, get_args_create_section_processor):
    actual = ZTOHFactory(get_config_map, persist_fs).get_processor(
        get_args_create_section_processor
    )
    assert isinstance(actual, CreateSectionProcessor)


def test_refresh_map_processor(get_config_map, get_args_refresh_map_processor):
    actual: RefreshMapProcessor = ZTOHFactory(get_config_map, persist_fs).get_processor(
        get_args_refresh_map_processor
    )
    assert isinstance(actual, RefreshMapProcessor)
