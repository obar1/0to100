# pylint: disable= R0904
import re

from zero_to_one_hundred.configs.ztoh_config_map import ZTOHConfigMap
from zero_to_one_hundred.models.readme_md import ReadMeMD
from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS
from zero_to_one_hundred.repository.ztoh_process_fs import ZTOHProcessFS
from zero_to_one_hundred.validator.validator import Validator
from zero_to_one_hundred.views.markdown_renderer import MarkdownRenderer


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
        process_fs: ZTOHProcessFS,
        http_url: str,
        is_done: bool = False,
    ):
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.http_url = http_url
        self.dir_name = Section.from_http_url_to_dir(http_url)
        self.dir_readme_md = (
            config_map.get_repo_path + "/" + self.dir_name + "/readme.md"
        )
        self.is_done = is_done

    def __repr__(self):
        return f"Section {self.http_url}  {self.dir_readme_md} {self.is_done} {self.dir_name}"

    def as_mark_down(self):
        return (
            "1. "
            + self.get_id_name
            + " [`here`]("
            + self.dir_readme_md
            + ")"
            + self.get_done_as_md
            + self.get_matching_icon_as_md
        )

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
        return self.find_header().strip("\n")

    @classmethod
    def from_http_url_to_dir(cls, http_url):
        return (
            http_url.replace("/", "§")
            .replace("<", "§")
            .replace(">", "§")
            .replace(":", "§")
            .replace("?", "§")
            .replace("*", "§")
            .replace("\\", "§")
        )

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
        return dir_name.replace("§", "/").replace("https///", "https://")

    @classmethod
    def done_section_status(cls, persist_fs, repo_path, dir_name):
        return persist_fs.done_section_status(repo_path, dir_name)

    @classmethod
    def build_from_http(cls, config_map, http_url, persist_fs, process_fs):
        return Section(config_map, persist_fs, process_fs, http_url)

    @classmethod
    def build_from_dir(
        cls, persist_fs, process_fs, config_map: ZTOHConfigMap, dir_name
    ):
        http_url = cls.from_http_url_to_dir_to(dir_name)
        return Section(
            config_map,
            persist_fs,
            process_fs,
            http_url,
            cls.done_section_status(persist_fs, config_map.get_repo_path, dir_name),
        )

    @classmethod
    def is_valid_dir(cls, curr_dir: str):
        return curr_dir.count("http") > 0

    def refresh_links(self):
        def convert(line):
            """convert to [https://](https:§§§...readme) or leave as it is"""
            res = line
            if str(line).strip("\n").startswith("https://"):
                res = (
                    "["
                    + str(line).strip("\n")
                    + "](../"
                    + Section(
                        self.config_map,
                        self.persist_fs,
                        self.process_fs,
                        str(line).strip("\n"),
                    ).dir_readme_md
                    + ")\n"
                )
            return res

        readme_md: ReadMeMD = ReadMeMD(
            self.config_map,
            self.persist_fs,
            self.process_fs,
            Section.from_http_url_to_dir,
            self.http_url,
        )
        lines_converted = []
        for line in readme_md.read():
            lines_converted.append(convert(line))
        readme_md.write(txt=lines_converted)

    def find_header(self):
        """
        take default header created by code or take first one # header found added by user
        """

        def get_header(line):
            if str(line).strip("\n").startswith("# "):
                return line
            return None

        readme_md: ReadMeMD = ReadMeMD(
            self.config_map,
            self.persist_fs,
            self.process_fs,
            Section.from_http_url_to_dir,
            self.http_url,
        )
        res = ""
        lines_converted = []
        try:
            for line in readme_md.read():
                lines_converted.append(get_header(line))
            headers = lines_converted
            not_null = list(filter(lambda x: x is not None, headers))
            if len(not_null) == 1:  # take default header
                res = not_null[0]
            if len(not_null) > 1:  # take first one header found
                res = not_null[1]
        except Exception as e:
            Validator.print_e(e)
            res = "FIXME: "
        return res

    @property
    def is_gcp_quest(self):
        return "quests" in self.http_url and "cloudskillsboost.google" in self.http_url

    @property
    def is_gcp_lab(self):
        return "labs" in self.http_url and "cloudskillsboost.google" in self.http_url

    @property
    def is_gcp_template(self):
        return (
            "course_templates" in self.http_url
            and "cloudskillsboost.google" in self.http_url
        )

    @property
    def is_gcp_game(self):
        return "games" in self.http_url and "cloudskillsboost.google" in self.http_url

    @property
    def is_datacamp_project(self):
        return "projects" in self.http_url and "app.datacamp.com" in self.http_url

    @property
    def is_datacamp_tutorial(self):
        return "tutorials" in self.http_url and "app.datacamp.com" in self.http_url

    @property
    def is_datacamp_course(self):
        return "courses" in self.http_url and "app.datacamp.com" in self.http_url

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
            other.http_oreilly_1 == self.http_url
            and other.dir_name == self.dir_name
            and other.dir_readme_md == self.dir_readme_md
            and other.is_done == self.is_done
        )
