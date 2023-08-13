"""Unit tests."""
# pylint: disable=R0913,W0613,W0613:,W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203

from main import run_main
from repository.process_fs import ProcessFS as process_fs


def test_run_main(
    mock_settings_env_vars,
    http_url,
    http_url_2,
    http_url_3,
    get_args_create_section_processor,
    get_args_done_section_processor,
    get_args_refresh_links_processor,
    get_args_refresh_puml_processor,
    get_args_refresh_map_processor,
    get_args_help_processor,
):
    """logical seq"""
    process_fs.debug_Y_N = True
    run_main(get_args_create_section_processor + [http_url])
    run_main(get_args_create_section_processor + [http_url_2])
    run_main(get_args_create_section_processor + [http_url_3])
    run_main(get_args_done_section_processor + [http_url_3])
    run_main(get_args_refresh_links_processor)
    run_main(get_args_refresh_map_processor)
    run_main(get_args_refresh_puml_processor)
    run_main(get_args_help_processor)
