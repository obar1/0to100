from abc import ABC, abstractmethod
import os
from zero_to_one_hundred.configs.a_config_map import AConfigMap

from zero_to_one_hundred.factories.a_factory import AFactory


class AFactoryProvider(ABC):
    """AFactoryProvider class."""

    def __init__(self, persist_fs, process_fs):
        self.MAP_YAML_PATH = os.getenv(AConfigMap.MAP_YAML_PATH)
        assert self.MAP_YAML_PATH is not None
        self.persist_fs = persist_fs
        self.process_fs = process_fs

    @abstractmethod
    def provide(self) -> AFactory:
        pass
