from zero_to_one_hundred.exceptions.errors import UnsupportedOptionError

from zero_to_one_hundred.processors.a_processor import AProcessor


class UnsupportedProcessor(AProcessor):
    """UnsupportedProcessor:
    std UnsupportedProcessor"""

    def __init__(self, cmd, supp):
        self.cmd = cmd
        self.supp = supp

    def process(self):
        supp_str = "`{}`".format("` `".join([s.name for s in self.supp]))
        raise UnsupportedOptionError(
            f"Unsupported Processor `{self.cmd}`, supported: {supp_str}"
        )
