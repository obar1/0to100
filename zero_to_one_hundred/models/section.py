from zero_to_one_hundred.configs.config_map import ConfigMap
from zero_to_one_hundred.models.readme_md import ReadMeMD


class Section:
    """Section:
    new_section od disk"""

    epub_suffix: str = ".epub"
    HTTP_OREILLY: str = "https://learning.oreilly.com/library/cover"
    GENERIC_HTTP_OREILLY: str = "https://learning.oreilly.com/library/"
    HTTTP_CLOUDSKILLSBOOST: str = "https://www.cloudskillsboost.google"

    def __init__(
        self,
        persist_fs,
        process_fs,
        config_map: ConfigMap,
        http_url: str,
        is_done: bool = False,
    ):
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.http_url = http_url
        self.dir_name = self.__from_dir_to_http_url(http_url)
        self.dir_readme_md = self.dir_name + "/readme.md"
        self.is_done = is_done

    def __repr__(self):
        return f"Section {self.http_url}, {self.dir_name}"

    @property
    def get_http_url(self):
        return self.http_url

    @property
    def get_done_as_md(self):
        return " :green_heart:" if self.is_done else " :footprints:"

    @property
    def get_dir_name(self):
        return self.dir_name

    @property
    def get_id_name(self):
        return self.find_header().strip("\n")

    @classmethod
    def __from_dir_to_http_url(cls, http_url):
        return (
            http_url.replace("/", "§")
            .replace("<", "§")
            .replace(">", "§")
            .replace(":", "§")
            .replace("?", "§")
            .replace("*", "§")
            .replace("\\", "§")
        )

    def write(self):
        return self.persist_fs.make_dirs(
            self.config_map.get_repo_path + "/" + self.dir_name
        )

    def write_done_section(self):
        return self.persist_fs.done_section(
            self.config_map.get_repo_path + "/" + self.dir_name
        )

    @classmethod
    def from_dir_to_http_url_to(cls, dir_name):
        return dir_name.replace("§", "/").replace("https///", "https://")

    @classmethod
    def done_section_status(cls, persist_fs, repo_path, dir_name):
        return persist_fs.done_section_status(repo_path, dir_name)

    @classmethod
    def build_from_http(cls, config_map, http_url, persist_fs, process_fs):
        return Section(persist_fs, process_fs, config_map, http_url)

    @classmethod
    def build_from_dir(cls, persist_fs, process_fs, config_map: ConfigMap, dir_name):
        http_url = cls.from_dir_to_http_url_to(dir_name)
        return Section(
            persist_fs,
            process_fs,
            config_map,
            http_url,
            cls.done_section_status(persist_fs, config_map.get_repo_path, dir_name),
        )

    @classmethod
    def is_valid_dir(cls, curr_dir: str):
        print(curr_dir)
        return curr_dir.count("http") > 0

    def refresh_links(self):
        def convert(line):
            """convert to [https://](https:§§§...readme) or leave as it is
            1 level only -assert"""
            res = line
            if str(line).strip("\n").startswith("https://"):
                res = (
                    "["
                    + str(line).strip("\n")
                    + "](../"
                    + Section(
                        self.persist_fs,
                        self.process_fs,
                        self.config_map,
                        str(line).strip("\n"),
                    ).dir_readme_md
                    + ")\n"
                )
            return res

        readme_md: ReadMeMD = ReadMeMD(
            self.persist_fs,
            self.process_fs,
            self.config_map,
            self.dir_name,
            self.http_url,
        )
        lines_converted = []
        for line in readme_md.read():
            lines_converted.append(convert(line))
        readme_md.write(txt=lines_converted)

    def find_header(self):
        def get_header(line):
            if str(line).strip("\n").startswith("# "):
                return line
            return None

        readme_md: ReadMeMD = ReadMeMD(
            self.persist_fs,
            self.process_fs,
            self.config_map,
            self.dir_name,
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
        except:
            print(readme_md)
            res = "TODO:"
        return res

    @property
    def is_quest(self):
        return "/quests" in self.http_url

    @property
    def is_lab(self):
        return "/labs" in self.http_url

    @property
    def is_template(self):
        return "/course_templates" in self.http_url

    @property
    def is_game(self):
        return "/games" in self.http_url

    @property
    def get_format_as_md(self):
        a = [
            ":cyclone:" if self.is_quest else None,
            ":floppy_disk:" if self.is_lab else None,
            ":whale:" if self.is_template else None,
            ":snake:" if self.is_game else None,
            ":pushpin:",
        ]
        return next(item for item in a if item is not None)

    @classmethod
    def get_legend_as_md(cls):
        return """
:cyclone: if is_quest
:floppy_disk: if is_lab
:whale: if is_template
:snake: if is_game
:pushpin: else

:green_heart: completed
:footprints: wip"""

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
