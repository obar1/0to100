"""CreateSectionProcessor:
create a new new_section on fs from http address
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
from typing import List

from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.models.map import Map
from zero_to_one_hundred.models.readme_md import ReadMeMD
from zero_to_one_hundred.models.section import Section


class CreateSectionProcessor:
    """CreateSectionProcessor."""

    def __init__(self, persist_fs, process_fs, config_map: SBConfigMap, http_url: str):
        """init"""
        self.http_url = http_url
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.config_map = config_map

    def process(self):
        """Process the new_section.
        - add new new_section
        - add def readme_md in new_section
        - add new sections to map at the end
        """
        section: Section = Section(
            self.persist_fs,
            self.process_fs,
            self.config_map,
            self.http_url,
            is_done=False,
        )
        section.write()
        readme_md: ReadMeMD = ReadMeMD(
            self.persist_fs,
            self.process_fs,
            self.config_map,
            section.dir_name,
            section.http_url,
        )
        readme_md.write()
        map_: Map = Map(self.persist_fs, self.config_map, self.get_sections(section))
        map_.write(False)

    def get_sections(self, new_section):
        """Get all the sections (sorted) and add the new new_section at the bottom"""
        dirs: List[str] = self.persist_fs.list_dirs(self.config_map.get_repo_path)
        if new_section.dir_name in dirs:
            dirs.remove(new_section.dir_name)
        if self.config_map.get_repo_sorted:
            sorted(dirs)
        dirs.append(new_section.dir_name)
        return Map.build_from_dirs(
            self.persist_fs, self.process_fs, self.config_map, dirs
        )
