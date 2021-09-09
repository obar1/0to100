"""TODO:
"""
# pylint: disable=R0903,E0401,W0703,W1201
import logging

from configs.config import Config, ConfigMap
from repository.persist_fs import PersistFS

class RefreshSectionsProcessor():

    def __init__(self, config_map:ConfigMap,PersistFS):
        self.config_map = config_map
        self.PersistFS = PersistFS

    def process(self):
        """Process the section."""
        return True