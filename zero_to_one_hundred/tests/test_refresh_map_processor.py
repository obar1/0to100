# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.processors.refresh_map_processor import RefreshMapProcessor
from zero_to_one_hundred.repository.process_fs import ProcessFS as process_fs
from zero_to_one_hundred.repository.persist_fs import PersistFS as persist_fs


def test_process(get_config_map, get_args_refresh_map_processor):
    actual: RefreshMapProcessor = ZTOHFactory(
        persist_fs, process_fs, get_config_map
    ).get_processor(get_args_refresh_map_processor)
    for p in actual:
        p.process()
