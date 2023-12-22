from abc import ABC, abstractmethod
from enum import Enum
from typing import Generator

from zero_to_one_hundred.processors.a_processor import AProcessor
from zero_to_one_hundred.processors.unsupported_processor import UnsupportedProcessor

# pylint: disable=R0801


class AFactory(ABC):
    """AFactory class."""

    class SUPPORTED_PROCESSOR(Enum):
        help = 1

    @abstractmethod
    def get_processor(self, args) -> Generator[AProcessor, None, None]:
        pass

    @staticmethod
    def unsupported_processor(cmd):
        return UnsupportedProcessor(cmd)
