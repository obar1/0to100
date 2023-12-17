"""FactoryProvider:
provides the actual factory based on the type value
"""

import os

from zero_to_one_hundred.configs.a_config_map import AConfigMap
from zero_to_one_hundred.configs.config_map import ConfigMap
from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory

MAP = "map"


class FactoryProvider:
    """FactoryProvider class.
    Provides factory implementation.
    """

    def __init__(self, persist_fs, process_fs):
        self.MAP_YAML_PATH = os.getenv(ConfigMap.MAP_YAML_PATH)
        assert self.MAP_YAML_PATH is not None
        self.persist_fs = persist_fs
        self.process_fs = process_fs

    def provide(self) -> ZTOHFactory:
        """T The method returns instance of MSEFactory."""
        get_type = AConfigMap(self.MAP_YAML_PATH, self.persist_fs).get_type
        if get_type == MAP:
            config_map = ConfigMap(self.persist_fs, self.MAP_YAML_PATH)
            return ZTOHFactory(self.persist_fs, self.process_fs, config_map)
        raise NotImplementedError(f"NotImplementedError {get_type}")
