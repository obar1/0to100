"""RefreshMapProcessor:
refresh section in map_
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203


class UnsupportedProcessor:
    """UnsupportedProcessor"""

    def __init__(self, cmd):
        self.cmd = cmd

    def process(self):
        logging.exception(f"Unsupported Processor {self.cmd}")
        raise ValueError
