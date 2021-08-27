"""Section processor.

A section is html address to study and save as md files
"""
# pylint: disable=R0903
from configs.config import Config


class SectionProcessor:
    """TODO."""

    def __init__(self, config: Config):
        self.__config = config

    def process(self):
        """Process the section."""
        print(self.__config)
        print("SectionProcessor.process")
