from zero_to_one_hundred.configs.ztoh_config_map import ZTOH_MAP, ZTOHConfigMap


# pylint: disable=W0621,W0613


def test_config_map(get_config_map: ZTOHConfigMap):
    actual = get_config_map
    assert actual.get_type == ZTOH_MAP
    assert actual.get_repo_path is not None
    assert actual.get_repo_map_md == "toc.md"
    assert actual.get_legend_type is None


def test_gcp_config_map(get_gcp_config_map: ZTOHConfigMap):
    actual = get_gcp_config_map
    assert actual.get_type == ZTOH_MAP
    assert actual.get_repo_path is not None
    assert actual.get_repo_map_md == "toc.md"
    assert actual.get_legend_type == "gcp"
    assert actual.get_legend_icons == [
        ZTOHConfigMap.LegendIcons("Path", ":cyclone:", "path"),
        ZTOHConfigMap.LegendIcons("Lab", ":floppy_disk:", "lab"),
        ZTOHConfigMap.LegendIcons("Template", ":whale:", "template"),
        ZTOHConfigMap.LegendIcons("Game", ":snake:", "game"),
        ZTOHConfigMap.LegendIcons("Course", ":pushpin:", "course"),
    ]


def test_datacamp_config_map(get_datacamp_config_map: ZTOHConfigMap):
    actual = get_datacamp_config_map
    assert actual.get_type == ZTOH_MAP
    assert actual.get_repo_path is not None
    assert actual.get_repo_map_md == "toc.md"
    assert actual.get_legend_type == "datacamp"
    assert actual.get_legend_icons == [
        ZTOHConfigMap.LegendIcons("Project", ":cyclone:", "project"),
        ZTOHConfigMap.LegendIcons("Tutorial", ":floppy_disk:", "tutorial"),
        ZTOHConfigMap.LegendIcons("Course", ":whale:", "course"),
    ]


def test_unsupported_config_map(get_unsupported_config_map: ZTOHConfigMap):
    actual = get_unsupported_config_map
    assert actual.get_type == "not-a-map"


def test_config_map_sorted_0(get_config_map_sorted_0: ZTOHConfigMap):
    actual = get_config_map_sorted_0
    assert actual.get_type == ZTOH_MAP
    assert actual.get_repo_path is not None
    assert actual.get_repo_sorted == "abc"
    assert actual.get_repo_map_md == "toc.md"
    assert actual.get_legend_type is None


def test_config_map_sorted_1(get_config_map_sorted_1: ZTOHConfigMap):
    actual = get_config_map_sorted_1
    assert actual.get_type == ZTOH_MAP
    assert actual.get_repo_path is not None
    assert actual.get_repo_sorted == "00:00:00"
    assert actual.get_repo_map_md == "toc.md"
    assert actual.get_legend_type is None
