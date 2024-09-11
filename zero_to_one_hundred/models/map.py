import logging
from typing import List

from zero_to_one_hundred.configs.ztoh_config_map import ZTOHConfigMap
from zero_to_one_hundred.models.section import Section
from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS
from zero_to_one_hundred.views.markdown_renderer import MarkdownRenderer


class Map(MarkdownRenderer):
    """Map:
    map md with list of sections as from fs"""

    def __init__(
        self,
        config_map: ZTOHConfigMap,
        persist_fs: ZTOHPersistFS,
        sections: List[Section],
    ):
        self.config_map = config_map
        self.readme_md = config_map.get_repo_map_md
        self.persist_fs = persist_fs
        self.sections = sections

    def __repr__(self):
        return f"Map {str(self.sections)}"

    def get_sections(self):
        res: List[Section] = self.sections
        if self.config_map.get_repo_sorted == "abc":
            logging.info("*** abc")
            res = sorted(self.sections, key=lambda s: s.dir_name)
        if self.config_map.get_repo_sorted == "00:00:00":
            logging.info("*** 00:00:00")
            res = sorted(self.sections, key=lambda s: s.get_readme_md_time())
        return res

    def as_mark_down(self) -> str:
        lf_char = "\n"

        def get_legend_as_md(self):
            txt: str = """## legend:
            """
            txt += lf_char
            txt += self.config_map.get_legend_icons_as_md
            return txt

        txt = f"""{f"# map {self.readme_md}, {len(self.sections)}"}

{get_legend_as_md(self)}

{lf_char.join((section.as_mark_down() for section in self.get_sections()))}
"""
        return txt.replace("  ", "")

    def write(self, txt: str):
        return self.persist_fs.write_file(self.readme_md, txt)

    @classmethod
    def build_from_dirs(
        cls, persist_fs, process_fs, config_map, dirs: List[str]
    ) -> List[Section]:
        """from a list of dirs created with Section() return the org Section()"""
        return [
            Section.build_from_dir(persist_fs, process_fs, config_map, curr_dir)
            for curr_dir in dirs
            if Section.is_valid_dir(curr_dir)
        ]
