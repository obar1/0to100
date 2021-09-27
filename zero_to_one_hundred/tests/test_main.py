"""Unit tests."""
# pylint: disable=C0116,R0903,E0401,W0703,W1201,redefined-outer-section,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203

from main import run_main


def test_run_main(
    get_args_create_section_processor,
    get_args_refresh_links_processor,
    get_args_refresh_puml_processor,
    get_args_refresh_map_processor,
):
    """logical seq"""
    run_main(get_args_create_section_processor + ["http://google.com/docs"])
    run_main(get_args_create_section_processor + ["https://cloud.google.com/docs"])
    run_main(
        get_args_create_section_processor + ["https://cloud.google.com/docs/overview"]
    )

    run_main(get_args_refresh_map_processor)
    run_main(get_args_refresh_links_processor)
    run_main(get_args_refresh_puml_processor)
