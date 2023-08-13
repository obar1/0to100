"""RefreshMapProcessor:
refresh sections in map
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging
import os

ROOT_DIR = os.path.dirname(os.path.abspath(
    __file__))  # This is your Project Root


class HelpProcessor:
    """HelpProcessor"""

    def __init__(self, persist_fs, supported_processor):
        """init"""
        self.supported_processor = supported_processor
        self.persist_fs = persist_fs

    def process(self):
        logging.debug([p.name for p in self.supported_processor])
