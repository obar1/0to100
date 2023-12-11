"""ProcessFS:
deal with Process
mocked in Test
"""

from datetime import datetime
import logging
import shlex
import subprocess

from zero_to_one_hundred.configs.config_map import ConfigMap


class SBProcessFS:
    """Process_fs."""

    DEBUG_ME = "echo"
    DEBUG_ME_NOT = ""
    DEBUG_Y_N = False

    @classmethod
    def debug_y_n(cls):
        return cls.DEBUG_ME if cls.DEBUG_Y_N else cls.DEBUG_ME_NOT

    @classmethod
    def write_img(cls, dir_img, http_url_img):
        logging.info(f"write_img  {dir_img} {http_url_img}")
        cmd = f'{cls.debug_y_n()} curl -o  "{dir_img}"  {http_url_img}'
        subprocess.call(shlex.split(cmd))

    @classmethod
    def write_epub(cls, config_map: ConfigMap, dir_epub, isbn):
        logging.info(f"write_epub {dir_epub} {isbn}")
        cls.download_epub(config_map, isbn)

    @classmethod
    def download_epub(cls, config_map, isbn):
        logging.info(f"download_epub {isbn}")
        cmd = f"{cls.debug_y_n()} python {config_map.get_download_engine_path} --cred {config_map.get_oreilly_username}:{config_map.get_oreilly_userpassword} {isbn}"
        proc = subprocess.run(cmd.split(), check=True)
        logging.info(proc.stdout)

    @staticmethod
    def get_now():
        return datetime.now().strftime("%Y/%m/%d-%H:%M:%S")
