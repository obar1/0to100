"""ReadMeMD:
a readme md with http and ref
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203

from configs.config import ConfigMap
from models.section import Section


class ReadMeMD:
    """ReadMeMD"""

    def __init__(self, persist_fs, process_fs, config_map: ConfigMap, section: Section):
        """init"""
        self.config_map = config_map
        self.readme_md = (
            config_map.get_repo_path + "/" + section.dir_name + "/readme.md"
        )
        self.section = section
        self.persist_fs = persist_fs
        self.process_fs = process_fs

    def __repr__(self):
        """repr"""
        return f"ReadMeMD {self.readme_md}, {self.section}"

    def write(self):
        """write to fs"""
        # # https§§§cloud.google.com§api-gateway§docs
        # > https://cloud.google.com/api-gateway/docs
        txt = []
        txt.append(
            f"""# <{self.section.dir_name}>
> <{self.section.http_url}>\n"""
        )
        return self.persist_fs.write_file(self.readme_md, txt)

    def refresh_links(self, txt):
        """refresh_links"""

        def convert(line):
            """convert to [http://](http:§§/...readme) or leave as it is"""
            if str(line).strip("\n").startswith("https://"):
                return (
                    "["
                    + str(line).strip("\n")
                    + "](/"
                    + Section(
                        self.persist_fs,
                        self.process_fs,
                        self.config_map,
                        str(line).strip("\n"),
                    ).dir_readme_md
                    + ")\n"
                )

            return line

        res = []
        for line in txt:
            res.append(convert(line))
        self.persist_fs.write_file(self.readme_md, res)

    def read(self):
        return self.persist_fs.read_file(self.readme_md)
