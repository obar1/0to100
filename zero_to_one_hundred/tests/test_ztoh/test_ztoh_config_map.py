from zero_to_one_hundred.configs.ztoh_config_map import ZTOH_MAP, ZTOHConfigMap


# pylint: disable=W0621,W0613


def test_config_map(get_config_map: ZTOHConfigMap):
    actual = get_config_map
    assert actual.get_type == ZTOH_MAP
    assert actual.get_repo_path is not None
    assert actual.get_repo_map_md == "toc.md"
    assert actual.get_repo_legend_type is None


def test__repr__(get_config_map: ZTOHConfigMap, get_map_yaml_path: str):
    actual = get_config_map
    assert (
        repr(actual)
        == f"MAP_YAML_PATH from {get_map_yaml_path} type {get_config_map.get_type}"
    )


def test_gcp_config_map(get_gcp_config_map: ZTOHConfigMap):
    actual = get_gcp_config_map
    assert actual.get_type == ZTOH_MAP
    assert actual.get_repo_path is not None
    assert actual.get_repo_map_md == "toc.md"
    assert actual.get_repo_legend_type == "gcp"


def test_datacamp_config_map(get_datacamp_config_map: ZTOHConfigMap):
    actual = get_datacamp_config_map
    assert actual.get_type == ZTOH_MAP
    assert actual.get_repo_path is not None
    assert actual.get_repo_map_md == "toc.md"
    assert actual.get_repo_legend_type == "datacamp"


def test_unsupported_config_map(get_unsupported_config_map: ZTOHConfigMap):
    actual = get_unsupported_config_map
    assert actual.get_type == "not-a-map"


def test_config_map_sorted_0(get_config_map_sorted_0: ZTOHConfigMap):
    actual = get_config_map_sorted_0
    assert actual.get_type == ZTOH_MAP
    assert actual.get_repo_path is not None
    assert actual.get_repo_sorted == "abc"
    assert actual.get_repo_map_md == "toc.md"
    assert actual.get_repo_legend_type is None


def test_config_map_sorted_1(get_config_map_sorted_1: ZTOHConfigMap):
    actual = get_config_map_sorted_1
    assert actual.get_type == ZTOH_MAP
    assert actual.get_repo_path is not None
    assert actual.get_repo_sorted == "00:00:00"
    assert actual.get_repo_map_md == "toc.md"
    assert actual.get_repo_legend_type is None
