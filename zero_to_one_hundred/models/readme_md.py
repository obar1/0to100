"""ReadMeMD:
a readme md with http and ref
"""
# pylint: disable=R0903,E0401,W0703,W1201
import logging

from configs.config import ConfigMap
from models.section import Section


class ReadMeMD:
    """ReadMeMD"""

    def __init__(self,config_map:ConfigMap, section:Section,PersistFS):
        self.readme_md=config_map.get_repo_path+ '/' + section.dir_name +'/readme.md'
        self.section=section
        self.PersistFS=PersistFS

    def __repr__(self):
        return  f"ReadMeMD {self.readme_md}, {self.section}"

    def write(self):
        # # https:§§cloud.google.com§api-gateway§docs
        # > https://cloud.google.com/api-gateway/docs
        txt = """
# {}
        
> {}
        """.format(self.section.dir_name,self.section.http_url)
        logging.warning(f"ReadMeMD - write {self}")
        return self.PersistFS.write_file(self.readme_md,txt)
