from src.zero_to_one_hundred.configs.sb_config_map import (
    SAFARI_BOOKS_MAP,
    SBConfigMap,
)

# pylint: disable=W0621,W0613


def test_provide__pass(get_config_map: SBConfigMap):
    actual = get_config_map
    assert actual.get_type == SAFARI_BOOKS_MAP
    assert actual.get_toc_path == "./0to100"
    assert actual.get_toc_fn_md == "toc_sb.md"
