from abc import ABC, abstractmethod


class AProcessor(ABC):
    """
    AProcessor"""

    @abstractmethod
    def __init__(self, config_map, persist_fs, process_fs, **kwargs):
        pass

    @abstractmethod
    def process(self):
        pass
