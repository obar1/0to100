"""DoneSectionProcessor:
done section on fs from http address
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203

from ast import List
from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.models.section import Section
from zero_to_one_hundred.models.map import Map


class DoneSectionProcessor:
    def __init__(self, persist_fs, process_fs, config_map: SBConfigMap, http_url: str):
        self.http_url = http_url
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.config_map = config_map

    def process(self):
        section: Section = Section(
            self.persist_fs,
            self.process_fs,
            self.config_map,
            self.http_url,
            is_done=True,
        )
        section.write_done_section()
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
