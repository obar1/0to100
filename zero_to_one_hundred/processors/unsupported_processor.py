from zero_to_one_hundred.exceptions.errors import UnsupportedOptionError

from zero_to_one_hundred.processors.a_processor import AProcessor


class UnsupportedProcessor(AProcessor):
    """UnsupportedProcessor:
    std UnsupportedProcessor"""

    def __init__(self, cmd):
        self.cmd = cmd

    def process(self):
        print(f"DDD Unsupported Processor {self.cmd}")
        raise UnsupportedOptionError("DDD Unsupported Processor {self.cmd}")
