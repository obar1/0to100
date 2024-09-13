from enum import Enum
from typing import Generator

from zero_to_one_hundred.processors.a_processor import AProcessor
from zero_to_one_hundred.processors.help_processor import HelpProcessor
from zero_to_one_hundred.processors.unsupported_processor import UnsupportedProcessor
from zero_to_one_hundred.repository.a_persist_fs import APersistFS


class AFactory:
    """AFactory class."""

    class SUPPORTED_PROCESSOR(Enum):
        zt = 1
        sb = 2
        help = 3

    def __init__(self, persist_fs: APersistFS):
        self.persist_fs = persist_fs

    def get_processor(self, args) -> Generator[AProcessor, None, None]:
        yield self.help_processor()

    def help_processor(self):
        return HelpProcessor(None, self.persist_fs, self.SUPPORTED_PROCESSOR)

    @staticmethod
    def unsupported_processor(cmd, supp):
        return UnsupportedProcessor(cmd, supp)
