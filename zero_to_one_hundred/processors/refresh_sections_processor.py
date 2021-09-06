"""Section processor.

A section is html address to study and save as md files
"""
# pylint: disable=R0903,W0238
import logging

from configs.config import Config
from repository.persist_fs import PersistFS

class RefreshSectionsProcessor():

    def __init__(self, config: Config, persist: PersistFS):
        self.__config = config
        self.__persist = persist

    def process(self):
        """Process the section."""
        pass