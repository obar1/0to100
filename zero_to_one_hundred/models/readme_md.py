from zero_to_one_hundred.repository.persist_fs import PersistFS

from zero_to_one_hundred.repository.process_fs import ProcessFS

from zero_to_one_hundred.configs.config_map import ConfigMap


class ReadMeMD:
    """ReadMeMD:
    a readme md with http and ref"""

    def __init__(self, config_map: ConfigMap, persist_fs: PersistFS, process_fs: ProcessFS, from_dir_to_http_url, http_url: str):
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.http_url = http_url
        self.dir_name = from_dir_to_http_url(http_url)
        self.readme_md = config_map.get_repo_path + "/" + self.dir_name + "/readme.md"


    def __repr__(self):
        return f"ReadMeMD {self.readme_md}, {self.dir_name} {self.http_url}"

    def write(self, txt=None):
        if txt is None:
            txt = []
            txt.append(f"""# <{self.dir_name}>\n> <{self.http_url}>\n""")
        return self.persist_fs.write_file(self.readme_md, txt)

    def read(self):
        return self.persist_fs.read_file(self.readme_md)
