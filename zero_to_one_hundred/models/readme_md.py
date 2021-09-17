"""ReadMeMD:
a readme md with http and ref
"""
# pylint: disable=R0903,E0401,W0703,W1201
import logging

from configs.config import ConfigMap
from models.section import Section
from repository.persist_fs import PersistFS


class ReadMeMD:
    """ReadMeMD"""

    def __init__(self,config_map:ConfigMap, section:Section,PersistFS):
        self.config_map=config_map
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
        return self.PersistFS.write_file(self.readme_md,txt)

    def refresh_links(self,txt):
        def f(line):
            if str(line).lstrip().startswith('https://'):
                return Section(self.config_map, str(line).lstrip(), self.PersistFS).dir_readme_md
            else:
                return line
        res=[]
        for line in txt:
            res.append(f(line))

        self.PersistFS.overwrite_file(self.readme_md,res)
        return res


    def read(self):
        return list(self.PersistFS.read_file(self.readme_md))
