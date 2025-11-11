from enum import Enum
from typing import Generator

from src.zero_to_one_hundred.processors.a_processor import (
    AProcessor,
)
from src.zero_to_one_hundred.processors.help_processor import (
    HelpProcessor,
)
from src.zero_to_one_hundred.processors.unsupported_processor import (
    UnsupportedProcessor,
)
from src.zero_to_one_hundred.repository.a_persist_fs import (
    APersistFS,
)

UV_RUN_MAIN: str = "uv run ./main.py"


class AFactory:
    """AFactory class."""

    class SUPPORTED_PROCESSOR(Enum):
        zo = 1
        sb = 2
        help = 3

    extended_help = f"""

    help = this :)
    {UV_RUN_MAIN} help

    zo = zero to 100
    {UV_RUN_MAIN} zo help

    sb = sb to 100
    {UV_RUN_MAIN} sb help
    """

    def __init__(self, persist_fs: APersistFS):
        self.persist_fs = persist_fs

    def get_processor(self, args) -> Generator[AProcessor, AProcessor, None]:
        yield self.help_processor()

    def help_processor(self):
        return HelpProcessor(
            None, self.persist_fs, self.SUPPORTED_PROCESSOR, self.extended_help
        )

    @staticmethod
    def unsupported_processor(cmd, supp):
        return UnsupportedProcessor(cmd, supp)
