"""TODO:
"""
# pylint: disable=R0903,E0401,W0703,W1201
from typing import List

from configs.config import ConfigMap
from models.map import Map
from models.section import Section
from models.readme_md import ReadMeMD
from processors.refresh_sections_processor import RefreshSectionsProcessor


class CreateSectionProcessor:
    """CreateSectionProcessor."""

    def __init__(self, config_map: ConfigMap, PersistFS, http_url:str):
        self.http_url = http_url
        self.PersistFS = PersistFS
        self.config_map=config_map

    def process(self):
        """Process the section.
        - add new section
        - add def readme_md in section
        - add new sections to map at the end
        """
        section:Section = Section(self.config_map, self.http_url,self.PersistFS)
        section.write()
        readme_md:ReadMeMD = ReadMeMD(self.config_map, section,self.PersistFS)
        readme_md.write()

        dirs:List[str]=self.PersistFS.list_dirs(self.config_map.get_repo_path)
        dirs.remove(section.dir_name)
        sorted(dirs)
        dirs.append(section.dir_name)
        sections=Map.build_from_dirs(self.config_map, self.PersistFS,dirs )
        map:Map = Map(self.config_map,self.PersistFS,sections)
        map.write(False)
