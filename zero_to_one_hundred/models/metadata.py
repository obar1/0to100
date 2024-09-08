import json

from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.repository.sb_persist_fs import SBPersistFS
from zero_to_one_hundred.repository.sb_process_fs import SBProcessFS
from zero_to_one_hundred.views.markdown_renderer import MarkdownRenderer


class Metadata(MarkdownRenderer):
    ONE_HUN_PER_TXT = "100.0%"

    DONE_TXT_AS_MD = '<span style="color:green">**DONE**</span>'
    WIP_TXT_AS_MD = '<span style="color:yellow">**WIP**</span>'

    def __init__(
        self,
        config_map: SBConfigMap,
        persist_fs: SBPersistFS,
        process_fs: SBProcessFS,
        get_isbn,
        http_url: str,
    ):
        self.config_map = config_map
        self.http_url = http_url
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.isbn = get_isbn(http_url)
        self.contents_path = persist_fs.abs_path(f"{self.isbn}")
        self.path_json = f"{self.contents_path}/{self.isbn}.json"
        self.metadata: dict = self.read()

    def __repr__(self):
        return f"MetaBook {self.isbn} {self.http_url} {self.as_mark_down()}"

    @staticmethod
    def get_page_perc(metadata_dict: dict):
        """
        given metadata_dict, get values of pages and return metadata_dict, n/a if no valid values are present
        """
        page_curr = int(metadata_dict.get("page_curr", "0"))
        pages_tot = int(metadata_dict.get("page_tot", "0"))
        perc = 0.0
        if pages_tot > 0:
            perc = 100 * page_curr / pages_tot
            return str(round(perc, 1)) + "%"
        return "n/a"

    def write(self):
        self.persist_fs.write_json(self.path_json, self.get_metadata())

    def read(self):
        try:
            json_data = self.persist_fs.read_file(self.path_json)
            lines = {} if json_data is None else json_data
            return json.loads("".join(lines))
        except:
            return {}

    @property
    def status(self):
        """use relative folder to simplify the usage in browser"""

        return (
            Metadata.DONE_TXT_AS_MD
            if self.get_metadata().get("pages_perc", None) == Metadata.ONE_HUN_PER_TXT
            else Metadata.WIP_TXT_AS_MD
        )

    def get_metadata(self):
        """
        refresh info for the final dict(), keys are orderered so it looks better :)
        """
        metadata_dict = self.metadata
        metadata_dict["isbn"] = self.isbn
        metadata_dict["url"] = (
            self.http_url if metadata_dict.get("url") is None else metadata_dict["url"]
        )  # keep it if found
        metadata_dict["pages_perc"] = self.get_page_perc(metadata_dict)
        sorted_dict = dict(sorted(metadata_dict.items()))
        return sorted_dict

    def as_mark_down(self) -> str:
        # handle nasty URL in MD
        m: dict = self.get_metadata()
        url = m.get("url")
        url = url.removeprefix("> ").removesuffix(" <")
        url = "> " + url + " <"
        m["url"] = url
        return MarkdownRenderer.text_lf_as_br(str(m))
