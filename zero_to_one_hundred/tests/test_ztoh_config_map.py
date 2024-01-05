from zero_to_one_hundred.configs.ztoh_config_map import ZTOH_MAP, ZTOHConfigMap

# pylint: disable=W0621,W0613


def test_pass_config_map(get_config_map: ZTOHConfigMap):
    actual = get_config_map
    assert actual.get_type == ZTOH_MAP
    assert actual.get_repo_path is not None
    assert actual.get_repo_sorted is False
    assert actual.get_repo_map_md == "toc.md"
    assert actual.get_repo_legend_type is None


def test__repr__(get_config_map: ZTOHConfigMap, get_map_yaml_path: str):
    actual = get_config_map
    assert (
        repr(actual)
        == f"MAP_YAML_PATH from {get_map_yaml_path} type {get_config_map.get_type}"
    )


def test_pass_gcp_config_map(get_gcp_config_map: ZTOHConfigMap):
    actual = get_gcp_config_map
    assert actual.get_type == ZTOH_MAP
    assert actual.get_repo_path is not None
    assert actual.get_repo_sorted is False
    assert actual.get_repo_map_md == "toc.md"
    assert actual.get_repo_legend_type == "gcp"


def test_pass_datacamp_config_map(get_datacamp_config_map: ZTOHConfigMap):
    actual = get_datacamp_config_map
    assert actual.get_type == ZTOH_MAP
    assert actual.get_repo_path is not None
    assert actual.get_repo_sorted is False
    assert actual.get_repo_map_md == "toc.md"
    assert actual.get_repo_legend_type == "datacamp"


def test_uns(get_unsupported_config_map: ZTOHConfigMap):
    # with pytest.raises(NotImplementedError):
    actual = get_unsupported_config_map
    assert actual.get_type == "not-a-map"
