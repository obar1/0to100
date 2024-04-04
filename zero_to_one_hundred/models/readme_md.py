from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS

from zero_to_one_hundred.repository.ztoh_process_fs import ZTOHProcessFS

from zero_to_one_hundred.configs.ztoh_config_map import ZTOHConfigMap
from zero_to_one_hundred.views.markdown_renderer import MarkdownRenderer


class ReadMeMD(MarkdownRenderer):
    """ReadMeMD:
    a readme md with http and ref"""

    def __init__(
        self,
        config_map: ZTOHConfigMap,
        persist_fs: ZTOHPersistFS,
        process_fs: ZTOHProcessFS,
        from_http_url_to_dir,
        http_url: str,
    ):
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.http_url = http_url
        self.dir_name = from_http_url_to_dir(http_url)
        self.readme_md = config_map.get_repo_path + "/" + self.dir_name + "/readme.md"

    def __repr__(self):
        return f"ReadMeMD {self.readme_md} {self.http_url} {self.dir_name}"

    def asMarkDown(self):
        return f"ReadMeMD {self.readme_md}, {self.dir_name} {self.http_url}"

    def write(self, txt=None):
        if txt is None:
            txt = []
            txt.append(f"""# <{self.dir_name}>\n> <{self.http_url}>\n""")
        return self.persist_fs.write_file(self.readme_md, txt)

    def read(self):
        data = self.persist_fs.read_file(self.readme_md)
        lines = "FIXME:" if data is None else data
        return lines
