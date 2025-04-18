import logging
import shlex
import subprocess

from zero_to_one_hundred.src.zero_to_one_hundred.configs.sb_config_map import (
    SBConfigMap,
)
from zero_to_one_hundred.src.zero_to_one_hundred.repository.ztoh_process_fs import (
    ZTOHProcessFS,
)


class SBProcessFS(ZTOHProcessFS):
    @classmethod
    def write_img(cls, path_img, http_url_img):
        logging.info(f"write_img  {path_img} {http_url_img}")
        cmd = f'curl -o  "{path_img}"  {http_url_img}'
        subprocess.run(shlex.split(cmd), check=True)
