from abc import ABC, abstractmethod
from zero_to_one_hundred.configs.a_config_map import AConfigMap


class AProcessor(ABC):
    """
    AProcessor"""

    @abstractmethod
    def __init__(self, persist_fs, process_fs, config_map: AConfigMap, **kwargs):
        pass

    @abstractmethod
    def process(self):
        pass
