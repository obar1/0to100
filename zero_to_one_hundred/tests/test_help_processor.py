# pylint: disable=C0116,R0903,E0401,W0703,W1201,redefined-outer-name,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203,W0613
from factories.ztoh_factory import ZTOHFactory
from processors.help_processor import HelpProcessor, VERSION
from tests.moke.persist_fs import PersistFS as persist_fs


def test_process(get_config_map, get_args_help_processor):
    actual: HelpProcessor = ZTOHFactory(get_config_map, persist_fs).get_processor(
        get_args_help_processor
    )
    curr_version = "1.0.1"
    assert actual.process() == f'{VERSION}"{curr_version}"'
