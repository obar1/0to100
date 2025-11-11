# pylint: disable= R0904
from loguru import logger as logging

import os
import re

from src.zero_to_one_hundred.configs.ztoh_config_map import (
    ZTOHConfigMap,
)
from src.zero_to_one_hundred.repository.ztoh_persist_fs import (
    ZTOHPersistFS,
)
from src.zero_to_one_hundred.validator.validator import Validator
from src.zero_to_one_hundred.views.markdown_renderer import (
    MarkdownRenderer,
)

YOUTUBE_HTTPS = "https://www.youtube."


class Section(MarkdownRenderer):
    """Section:
    new_section od disk"""

    epub_suffix: str = ".epub"
    HTTP_OREILLY: str = "https://learning.oreilly.com/library/cover"
    GENERIC_HTTP_OREILLY: str = "https://learning.oreilly.com/library/"

    def __init__(
        self,
        config_map: ZTOHConfigMap,
        persist_fs: ZTOHPersistFS,
        http_url: str,
        is_done: bool = False,
    ):
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.http_url = http_url
        self.dir_name = Section.from_http_url_to_dir(http_url)
        self.dir_readme_md = (
            config_map.get_repo_path + "/" + self.dir_name + "/readme.md"
        )
        self.is_done = is_done

    def __repr__(self):
        return f"Section {self.http_url}  {self.dir_readme_md} {self.is_done} {self.dir_name}"

    def as_mark_down(self):
        res = ""
        res += (
            "1. "
            + self.get_id_name
            + " [`here`]("
            + self.dir_readme_md
            + ")"
            + self.get_done_as_md
            + self.get_matching_icon_as_md
        )
        return res

    @property
    def get_http_url(self):
        return self.http_url

    @property
    def get_done_as_md(self):
        return " `done` " if self.is_done else " `wip` "

    @property
    def get_dir_name(self):
        return self.dir_name

    @property
    def get_id_name(self):
        """scan the contents, it return the 1st or 2nd occurrence
        of
        # some txt

        Returns:
            str: header
        """
        res = "# TODO: Add an Header"
        try:
            with open(self.dir_readme_md, "r") as file:
                lines = file.readlines()

                count = 0
                for line in lines:
                    if line.strip().startswith("# "):
                        count += 1
                        if count <= 2:
                            res = line.strip()
        except Exception as e:
            Validator.print_e(e)
        return res

    @classmethod
    def from_http_url_to_dir(cls, http_url):
        chars_to_replace = r"/<>?:*\#="
        replacement_char = "§"
        translation_table = str.maketrans(
            chars_to_replace, replacement_char * len(chars_to_replace)
        )
        return http_url.translate(translation_table)

    def write(self, txt: str):
        return self.persist_fs.make_dirs(txt)

    def write_done_section(self):
        return self.persist_fs.done_section(
            self.config_map.get_repo_path + "/" + self.dir_name
        )

    def get_readme_md_time(self):
        return self.persist_fs.get_biz_ts(self.dir_readme_md)

    @classmethod
    def from_http_url_to_dir_to(cls, dir_name):
        """try to restore http for what it is possible"""
        return dir_name.replace("§", "/").replace("https///", "https://")

    @classmethod
    def done_section_status(cls, persist_fs, repo_path, dir_name):
        return persist_fs.done_section_status(repo_path, dir_name)

    @classmethod
    def build_from_http(cls, config_map, http_url, persist_fs):
        return Section(config_map, persist_fs, http_url)

    @classmethod
    def build_from_dir(cls, persist_fs, config_map: ZTOHConfigMap, dir_name):
        http_url = cls.from_http_url_to_dir_to(dir_name)
        return Section(
            config_map,
            persist_fs,
            http_url,
            cls.done_section_status(persist_fs, config_map.get_repo_path, dir_name),
        )

    @classmethod
    def is_valid_dir(cls, curr_dir: str):
        return curr_dir.count("http") > 0

    def materialize_https(self, line):
        """convert to [https://](https:§§§...readme) or leave as it is"""
        res = line
        if str(line).strip("\n").startswith("https://"):
            up_folder = ".."
            dir_readme_md_abs = Section(
                self.config_map,
                self.persist_fs,
                str(line).strip("\n"),
            ).dir_readme_md.replace(self.config_map.get_repo_path, "")
            res = (
                "["
                + str(line).strip("\n")
                + "]("
                + up_folder
                + dir_readme_md_abs
                + ")\n"
            )
        return res

    def look_for_materialized_https(self):
        lines_converted = []
        for line in self.persist_fs.read_file(self.dir_readme_md):
            lines_converted.append(self.materialize_https(line))
        self.persist_fs.write_file(filename=self.dir_readme_md, txt=lines_converted)

    def look_for_orphan_images(self, lines, png_files):
        pattern = r"!\[[^\]]*\]\(([^)]+)\)"
        matches = re.findall(pattern, "".join(lines))
        referenced_images = [
            str(m).removeprefix("![alt text](").removesuffix(")") for m in matches
        ]

        orphan_images = []
        for png_file in png_files:
            if png_file not in referenced_images:
                orphan_images.append(png_file)
        return orphan_images

    def delete_orphan_images(self):
        readme_md_dir = self.config_map.get_repo_path + "/" + self.dir_name
        get_png_files = [
            f for f in os.listdir(readme_md_dir) if f.lower().endswith(".png")
        ]
        lines = self.persist_fs.read_file(self.dir_readme_md)
        if len(get_png_files) > 0:
            png_files_to_delete = self.look_for_orphan_images(lines, get_png_files)
            for f in png_files_to_delete:
                logging.warning(f"delete_orphan_images {f}")
                os.remove(readme_md_dir + "/" + f)

    @property
    def get_matching_icon_as_md(self):
        icons = self.config_map.get_legend_icons

        res = [i.icon for i in icons if re.search(i.regex, self.http_url)]
        return " ".join(res)

    def __eq__(self, other):
        if other is self:
            return True

        if type(other) is not type(self):
            # delegate to superclass
            return NotImplemented

        return (
            other.http_url == self.http_url
            and other.dir_name == self.dir_name
            and other.dir_readme_md == self.dir_readme_md
            and other.is_done == self.is_done
        )
