"""Section processor.

A section is html address to study and save as md files
"""
# pylint: disable=R0903,W0238
import logging
from pprint import pprint
from typing import List

from configs.config import Config
from models.section import Section
from repository.persist_fs import PersistFS


class CreateSectionProcessor:
    """TODO."""

    def __init__(self, config: Config, http_url, persist: PersistFS):
        self.__config = config
        self.__http_url = http_url
        self.__persist = persist

    def process(self):
        """Process the section."""
        sections_in_map: List[Section] = self.__persist.load_map()

        section = Section(self.__http_url)
        logging.info(str(section))

        assert section not in sections_in_map
        self.__persist.write(section)

