"""ProcessFS:
deal with Process
mocked in Test
"""
# pylint: disable=C0301,W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging
import shlex
import subprocess

from zero_to_one_hundred.configs.config_map import ConfigMap


class ProcessFS:
    """Process_fs."""

    info_ME = "echo"
    info_ME_NOT = ""
    info_Y_N = False

    @classmethod
    def info_y_n(cls):
        return cls.info_ME if cls.info_Y_N else cls.info_ME_NOT

    @classmethod
    def write_img(cls, dir_img, http_url_img):
        logging.info(f"write_img  {dir_img} {http_url_img}")
        cmd = f"{cls.info_y_n()} curl -o  {dir_img}  {http_url_img}"
        subprocess.call(shlex.split(cmd))

    @classmethod
    def write_epub(cls, config_map: ConfigMap, dir_epub, isbn):
        logging.info(f"write_epub {dir_epub} {isbn}")
        cls.download_epub(config_map, isbn)

    @classmethod
    def download_epub(cls, config_map, isbn):
        logging.info(f"download_epub {isbn}")
        cmd = f"{cls.info_y_n()} python {config_map.get_download_engine_path} --cred {config_map.get_oreilly_username}:{config_map.get_oreilly_userpassword} {isbn}"
        proc = subprocess.run(cmd.split(), check=True)
        logging.info(proc.stdout)
