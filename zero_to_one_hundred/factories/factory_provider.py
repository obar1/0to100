# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203

import os

from zero_to_one_hundred.configs.config import Config
from zero_to_one_hundred.configs.config_map import ConfigMap
from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory

MAP = "map"

MAP_YAML_PATH = "MAP_YAML_PATH"


class FactoryProvider:
    """FactoryProvider class.
    Provides factory implementation.
    """

    def __init__(self, persist_fs, process_fs):
        self.MAP_YAML_PATH = os.getenv(MAP_YAML_PATH)
        assert self.MAP_YAML_PATH is not None
        print(f"using MAP_YAML_PATH: {self.MAP_YAML_PATH}")
        self.persist_fs = persist_fs
        self.process_fs = process_fs

    def provide(self) -> ZTOHFactory:
        """T The method returns instance of MSEFactory."""
        get_type = Config(self.MAP_YAML_PATH, self.persist_fs).get_type
        if get_type == MAP:
            config_map = ConfigMap(self.persist_fs, self.MAP_YAML_PATH)
            return ZTOHFactory(self.persist_fs, self.process_fs, config_map)
        raise NotImplementedError(f"NotImplementedError {get_type}")
