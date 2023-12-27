from abc import ABC, abstractmethod

from zero_to_one_hundred.configs.a_config_map import AConfigMap


class AProcessor(ABC):
    """
    AProcessor"""

    @abstractmethod
    def __init__(self, config_map, persist_fs, process_fs, **kwargs):
        pass

    @abstractmethod
    def process(self):
        pass
