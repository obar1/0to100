from zero_to_one_hundred.configs.ztoh_config_map import ZTOH_MAP

# pylint: disable=W0621,W0613


def test_pass(get_config_map):
    actual = get_config_map
    assert actual.get_type == ZTOH_MAP
    assert actual.get_repo_path is not None
    assert actual.get_repo_sorted is False
    assert actual.get_repo_map_md == "0to100.md"


def test__repr__(get_config_map, get_map_yaml_path):
    actual = get_config_map
    assert (
        repr(actual)
        == f"MAP_YAML_PATH from {get_map_yaml_path} type {get_config_map.get_type}"
    )
