"""RefreshMapProcessor:
refresh section in map_
"""


class UnsupportedProcessor:
    def __init__(self, cmd):
        self.cmd = cmd

    def process(self):
        print(f"Unsupported Processor {self.cmd}")
        raise ValueError
