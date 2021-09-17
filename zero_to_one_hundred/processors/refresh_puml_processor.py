from configs.config import ConfigMap
from models.map import Map
from models.puml import PUML


class RefreshPUMLProcessor:



    def __init__(self, config_map: ConfigMap, PersistFS):
        self.config_map = config_map
        self.PersistFS = PersistFS

    def process(self):
        """Scan the repo and for each section add it to the puml, save the map file."""
        sections=Map.build_from_dirs(self.config_map, self.PersistFS, self.PersistFS.list_dirs(self.config_map.get_repo_path))
        puml:PUML = PUML(self.config_map,self.PersistFS,sections)
        puml.write()