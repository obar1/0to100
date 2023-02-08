"""FactoryProvider:
provides the actual factory based on the type value
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203

import os

from configs.config import Config, ConfigMap
from factories.ztoh_factory import ZTOHFactory

MAP = "map"

CONFIG_FILE = "CONFIG_FILE"


class FactoryProvider:
    """FactoryProvider class.
    Provides factory implementation.
    """

    def __init__(self, persist_fs, process_fs):
        """init"""
        self.config_file = os.getenv(CONFIG_FILE)
        self.persist_fs = persist_fs
        self.process_fs = process_fs

    def provide(self) -> ZTOHFactory:
        """T The method returns instance of MSEFactory."""
        get_type = Config(self.config_file, self.persist_fs).get_type
        if get_type == MAP:
            config_map = ConfigMap(self.persist_fs, self.config_file)
            return ZTOHFactory(self.persist_fs, self.process_fs, config_map)
        raise NotImplementedError(f"NotImplementedError {get_type}")
