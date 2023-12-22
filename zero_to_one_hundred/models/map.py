from typing import Callable, List
from connect.utils.terminal.markdown import render

from zero_to_one_hundred.configs.config_map import ConfigMap
from zero_to_one_hundred.models.section import Section


class Map:
    """Map:
    map md with list of sections as from fs"""

    def __init__(self, persist_fs, config_map: ConfigMap, sections: List[Section]):
        self.config_map = config_map
        self.readme_md = config_map.get_repo_path + "/" + config_map.get_repo_map_md
        self.persist_fs = persist_fs
        self.sections = sections

    def __repr__(self):
        return f"Map {self.readme_md}, {self.sections}"

    @staticmethod
    def __repr_flatten(sections: List[Section], as_sorted: bool) -> str:
        # 1. <https://cloud.google.com/api-gateway/docs/about-ap
        # i-gateway> :ok: [`here`](../https§§§cloud.google.com§/readme.md)
        print(as_sorted)
        lambda_flatten_section: Callable[[Section], str] = (
            lambda s: "1. "
            + s.get_id_name
            + " [`here`]("
            + s.get_dir_name
            + "/readme.md)"
            + s.get_done_as_md
            + " "
            + s.get_format_as_md
        )
        flattened_sections = list(map(lambda_flatten_section, sections))
        return "\n".join(flattened_sections)

    def write(self, as_sorted):
        # init with list of sections found
        txt = []
        txt.append(
            f"""
# {self.readme_md}

> sorted:{self.config_map.get_repo_sorted}

> legend:{Section.get_legend_as_md()}

{self.__repr_flatten(self.sections, as_sorted)}
        """
        )
        print(render("\n".join(txt)))
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
