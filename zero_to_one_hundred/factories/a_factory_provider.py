from abc import ABC, abstractmethod

from zero_to_one_hundred.factories.a_factory import AFactory
from zero_to_one_hundred.repository.a_persist_fs import APersistFS


class AFactoryProvider(ABC):
    """AFactoryProvider."""

    @abstractmethod
    def __init__(self, persist_fs: APersistFS, process_fs):
        pass

    @abstractmethod
    def provide(self) -> None | AFactory:
        pass
