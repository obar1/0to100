from dataclasses import dataclass
from zero_to_one_hundred.configs.a_config_map import AConfigMap
from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS

ZTOH_MAP = "ztoh-map"


class ZTOHConfigMap(AConfigMap):

    @dataclass
    class LegendIcons:
        name: str
        icon: str
        regex:str 
        
    def __init__(self, persist_fs: ZTOHPersistFS):
        super().__init__(persist_fs)

    @property
    def get_repo_path(self):
        return self.load["repo"]["path"]

    @property
    def get_repo_map_md(self):
        return self.load["repo"]["map_md"]

    @property
    def get_repo_sorted(self) -> bool:
        return self.load["repo"].get("sorted")

    @property
    def get_legend_type(self) -> str | None:
        return None if self.load.get("legend") is None else self.load.get("legend").get("type")

    @property
    def get_legend_icons(self):
        legend =  self.load.get("legend")
        if legend:
            return [
        ZTOHConfigMap.LegendIcons(name=icon_data['name'], icon=icon_data['icon'], regex=icon_data['regex'])
        for icon_data in legend.get('icons', [])
        if isinstance(icon_data, dict)]
        return []

    @property
    def get_legend_icons_as_md(self):
        icons = self.get_legend_icons
        res = [f"`{i.name}` {i.icon}" for i in icons]
        return  "\n".join(res)
