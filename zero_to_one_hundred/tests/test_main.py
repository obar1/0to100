"""Unit tests."""
# pylint: disable=C0116,R0903,E0401,W0703,W1201,redefined-outer-name,missing-function-docstring,E0401,C0114,W0511,C0209,W1203,C0200,C0103
import pytest

from main import run_main


def test_version(get_version):
    expected = "0.0.5"
    with open(get_version, mode="r", encoding="UTF-8") as file_handle:
        assert file_handle.read().lower().strip("\n") == expected


@pytest.mark.skip
def test_run_main(get_create_section_params, get_refresh_map_params):
    """logical seq"""
    run_main(get_create_section_params)
    run_main(get_refresh_map_params)
