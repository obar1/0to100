"""TODO:
"""
# pylint: disable=R0903,E0401,W0703,W1201
from configs.config import ConfigMap
from models.section import Section


class ReadMeMD:

    def __init__(self,config_map:ConfigMap, section:Section,PersistFS):
        self.readme_md=config_map.get_repo_path+"/readme.md"
        self.section=section
        self.PersistFS=PersistFS


    def write(self):
        # # https:§§cloud.google.com§api-gateway§docs
        # > https: // cloud.google.com / api - gateway / docs
        txt = """
# {}
        
> {}
        """.format(self.section.dir_name,self.section.http_url)
        return self.PersistFS.write_file(self.readme_md,txt)
