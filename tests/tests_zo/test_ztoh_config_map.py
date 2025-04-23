from src.zero_to_one_hundred.configs.ztoh_config_map import (
    ZTOH_MAP,
    ZTOHConfigMap,
)

# pylint: disable=W0621,W0613


def test_config_map(get_config_map: ZTOHConfigMap):
    actual = get_config_map
    assert actual.get_type == ZTOH_MAP
    assert actual.get_repo_path is not None
    assert actual.get_repo_map_md == "toc_zo.md"
    assert actual.get_legend_type is None


def test_unsupported_config_map(get_unsupported_config_map: ZTOHConfigMap):
    actual = get_unsupported_config_map
    assert actual.get_type == "unsupported-map"


def test_config_map_sorted_0(get_config_map_sorted_0: ZTOHConfigMap):
    actual = get_config_map_sorted_0
    assert actual.get_type == ZTOH_MAP
    assert actual.get_repo_path is not None
    assert actual.get_repo_sorted == "abc"
    assert actual.get_repo_map_md == "toc_zo.md"
    assert actual.get_legend_type is None


def test_config_map_sorted_1(get_config_map_sorted_1: ZTOHConfigMap):
    actual = get_config_map_sorted_1
    assert actual.get_type == ZTOH_MAP
    assert actual.get_repo_path is not None
    assert actual.get_repo_sorted == "00:00:00"
    assert actual.get_repo_map_md == "toc_zo.md"
    assert actual.get_legend_type is None
