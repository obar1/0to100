from zero_to_one_hundred.exceptions.errors import UnsupportedOptionError

from zero_to_one_hundred.processors.a_processor import AProcessor


class UnsupportedProcessor(AProcessor):
    """UnsupportedProcessor:
    std UnsupportedProcessor"""

    def __init__(self, cmd, supp):
        self.cmd = cmd
        self.supp = supp

    def process(self):
        raise UnsupportedOptionError(
            f"Unsupported Processor {self.cmd}, supported {[x.name for x in self.supp]}"
        )
