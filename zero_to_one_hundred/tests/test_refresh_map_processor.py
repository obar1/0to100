# pylint: disable=C0116,R0903,E0401,W0703,W1201,redefined-outer-section,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
from factories.ztoh_factory import ZTOHFactory
from processors.refresh_map_processor import RefreshMapProcessor
from tests.moke.persist_fs import PersistFS as persist_fs


def test_process(get_config_map, get_args_refresh_map_processor):
    actual: RefreshMapProcessor = ZTOHFactory(get_config_map, persist_fs).get_processor(
        get_args_refresh_map_processor
    )
    actual.process()
