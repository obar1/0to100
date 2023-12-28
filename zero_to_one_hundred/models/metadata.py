import json
import sys
from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.repository.sb_persist_fs import SBPersistFS as persist_fs
from zero_to_one_hundred.repository.sb_process_fs import SBProcessFS as process_fs

class Metadata:
    def __init__(
        self,
        get_isbn,
        config_map: SBConfigMap,
        persist_fs:persist_fs,
        process_fs:process_fs,
        http_url: str,
        page_curr=0,
        pages_tot=0,
    ):
        self.config_map = config_map
        self.http_url = http_url
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.page_curr = page_curr
        self.pages_tot = pages_tot
        self.isbn = get_isbn(http_url)
        self.contents_path = persist_fs.abs_path(f"{self.isbn}")
        self.path_json = f"{self.contents_path}/{self.isbn}.json"

    def __repr__(self):
        return f"Metadata {self.http_url}, {self.isbn} {self.contents_path}"

    @property
    def get_page_perc(self):
        perc = 0
        if self.pages_tot > 0:
            perc = 100 * self.page_curr / self.pages_tot
        return str(round(perc, 1)) + "%"

    def write(self):
        self.persist_fs.make_dirs(self.contents_path)
        self.write_json()

    def read_json(self):
        lines = "{}"
        try:
            lines = self.persist_fs.read_file(self.path_json)
            return json.dumps(json.loads("".join(lines)), indent=4)
        except:
            return lines

    def write_json(self):
        """write json
        {
            "isbn": "0596007124",
            "http_url": "https://learning.oreilly.com/library/view/head-first-design/0596007124/"
        }
        """
        txt = []
        txt.append(
            "{"
            + ' "isbn" : "'
            + self.isbn
            + '" '
            + ' ,"url" : "'
            + self.http_url
            + '" '
            + "}"
        )
        self.persist_fs.write_file(
            self.path_json, json.dumps(json.loads("".join(txt)), indent=4)
        )

    def read_json(self):
        lines = "{}"
        try:
            lines = self.persist_fs.read_file(self.path_json)
            return json.dumps(json.loads("".join(lines)), indent=4)
        except:
            return lines
