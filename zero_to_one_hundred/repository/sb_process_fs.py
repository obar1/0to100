import shlex
import subprocess

from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.repository.process_fs import ProcessFS


class SBProcessFS(ProcessFS):
    @classmethod
    def write_img(cls, path_img, http_url_img):
        print(f"write_img  {path_img} {http_url_img}")
        cmd = f'curl -o  "{path_img}"  {http_url_img}'
        subprocess.run(shlex.split(cmd), check=True)

    @classmethod
    def write_epub(cls, config_map: SBConfigMap, path_epub, isbn):
        print(f"write_epub {path_epub} {isbn}")
        cmd = f"python {config_map.get_download_engine_path} --cred {config_map.get_oreilly_username}:{config_map.get_oreilly_userpassword} {isbn}"
        subprocess.run(cmd.split(), check=True)
