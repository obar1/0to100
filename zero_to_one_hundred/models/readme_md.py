"""ReadMeMD:
a readme md with http and ref
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203

from configs.config import ConfigMap


class ReadMeMD:
    """ReadMeMD"""

    def __init__(
        self, persist_fs, process_fs, config_map: ConfigMap, dir_name, http_url
    ):
        """init"""
        self.config_map = config_map
        self.readme_md = config_map.get_repo_path + "/" + dir_name + "/readme.md"
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.dir_name = dir_name
        self.http_url = http_url

    def __repr__(self):
        """repr"""
        return f"ReadMeMD {self.readme_md}, {self.dir_name} {self.http_url}"

    def write(self, txt=None):
        """write to fs"""
        # # https§§§cloud.google.com§api-gateway§docs
        # > https://cloud.google.com/api-gateway/docs
        if txt is None:
            txt = []
            txt.append(
                f"""# <{self.dir_name}>\n><{self.http_url}>\n"""
            )
        return self.persist_fs.write_file(self.readme_md, txt)

    def read(self):
        return self.persist_fs.read_file(self.readme_md)
