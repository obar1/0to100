from src.zero_to_one_hundred.configs.ztoh_config_map import (
    ZTOHConfigMap,
)
from src.zero_to_one_hundred.repository.ztoh_persist_fs import (
    ZTOHPersistFS,
)
from src.zero_to_one_hundred.views.markdown_renderer import (
    MarkdownRenderer,
)


class ReadMeMD(MarkdownRenderer):
    """ReadMeMD:
    a readme md with http and ref"""

    def __init__(
        self,
        config_map: ZTOHConfigMap,
        persist_fs: ZTOHPersistFS,
        from_http_url_to_dir,
        http_url: str,
    ):
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.http_url = http_url
        self.dir_name = from_http_url_to_dir(http_url)
        self.readme_md = config_map.get_repo_path + "/" + self.dir_name + "/readme.md"

    def __repr__(self):
        return f"ReadMeMD {self.readme_md} {self.http_url} {self.dir_name}"

    def as_mark_down(self):
        return f"ReadMeMD {self.readme_md}, {self.dir_name} {self.http_url}"

    def write(self):
        txt = []
        txt.append(f"""# <{self.dir_name}>\n> <{self.http_url}>\n""")
        return self.persist_fs.write_file(self.readme_md, txt)

    def read(self):
        data = self.persist_fs.read_file(self.readme_md)
        lines = "_FIXME_" if data is None else data
        return lines
