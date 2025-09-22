import json
from loguru import logger as logging

import shlex
import subprocess

from src.zero_to_one_hundred.repository.ztoh_persist_fs import (
    ZTOHPersistFS,
)

PREFIX_RELATIVE_FOLDER = "./"

# pylint: disable=E1205,W1201


class SBPersistFS(ZTOHPersistFS):
    """SBPersistFS:
    deal with FS
    """

    @classmethod
    def is_relative_path(cls, path):
        if str(path).startswith(PREFIX_RELATIVE_FOLDER):
            return True
        return False

    @classmethod
    def render_json(cls, txt: str):
        return txt.replace('"', ' " ').replace("\n", " <br/> ")

    @classmethod
    def write_json(cls, path_json: str, txt: dict):
        logging.info(f"write_json {path_json} {txt}")
        ZTOHPersistFS.write_file_json(path_json, txt)

    @classmethod
    def read_pages_curr(cls, fn: str) -> int:
        logging.info(f"read_pages_curr {fn}")
        with open(fn, "r", encoding="utf-8") as f:
            json_data = json.loads(f.read())
            logging.info(json_data)
            return int(json_data["page_curr"])

    @classmethod
    def write_img(cls, path_img, http_url_img):
        logging.info(f"write_img  {path_img} {http_url_img}")
        cmd = f'curl -o  "{path_img}"  {http_url_img}'
        subprocess.run(shlex.split(cmd), check=True)
