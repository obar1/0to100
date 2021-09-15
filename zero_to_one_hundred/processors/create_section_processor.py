"""TODO:
"""
# pylint: disable=R0903,E0401,W0703,W1201
import logging
from pprint import pprint
from typing import List

from configs.config import ConfigMap
from models.section import Section
from repository.readmemd import ReadMeMD


class CreateSectionProcessor:
    """CreateSectionProcessor."""

    def __init__(self, config_map: ConfigMap, PersistFS, http_url:str):
        self.http_url = http_url
        self.PersistFS = PersistFS
        self.config_map=config_map

    def process(self):
        """Process the section."""
        section:Section = Section(self.config_map, self.http_url,self.PersistFS)
        section.write()
        readme_md:ReadMeMD = ReadMeMD(self.config_map, section,self.PersistFS)
        readme_md.write()
        return True