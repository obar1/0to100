import shlex
import subprocess

from zero_to_one_hundred.configs.config_map import ConfigMap
from zero_to_one_hundred.repository.process_fs import ProcessFS


class SBProcessFS(ProcessFS):
    @classmethod
    def write_img(cls, dir_img, http_url_img):
        print(f"write_img  {dir_img} {http_url_img}")
        cmd = f'curl -o  "{dir_img}"  {http_url_img}'
        subprocess.run(shlex.split(cmd), check=True)

    @classmethod
    def write_epub(cls, config_map: ConfigMap, dir_epub, isbn):
        print(f"write_epub {dir_epub} {isbn}")
        cmd = f"python {config_map.get_download_engine_path} --cred {config_map.get_oreilly_username}:{config_map.get_oreilly_userpassword} {isbn}"
        subprocess.run(cmd.split(), check=True)
