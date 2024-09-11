# pylint: disable=W0246
import os
from abc import ABC
from dataclasses import dataclass

from zero_to_one_hundred.exceptions.errors import SomeError
from zero_to_one_hundred.repository.a_persist_fs import APersistFS


class AConfigMap(ABC):
    MAP_YAML_PATH = "MAP_YAML_PATH"

    @dataclass
    class LegendIcons:
        name: str
        icon: str
        regex: str

    def __init__(self, persist_fs: APersistFS):
        self.map_yaml_path = os.getenv(AConfigMap.MAP_YAML_PATH)
        if self.map_yaml_path is None:
            raise SomeError(
                f"map_yaml_path {self.map_yaml_path} is not valid,\nplease set it in the env ex:\n`export MAP_YAML_PATH=map.yaml`"
            )
        self.persist_fs = persist_fs

    def __repr__(self):
        return (
            f"{AConfigMap.MAP_YAML_PATH} from {self.map_yaml_path} type {self.get_type}"
        )

    @property
    def load(self):
        return self.persist_fs.load_map_yaml_path(self.map_yaml_path)

    @property
    def get_type(self):
        return self.load["type"]

    @property
    def get_legend_icons(self):
        legend = self.load.get("legend")
        if legend:
            return [
                AConfigMap.LegendIcons(
                    name=icon_data["name"],
                    icon=icon_data["icon"],
                    regex=icon_data["regex"],
                )
                for icon_data in legend.get("icons", [])
                if isinstance(icon_data, dict)
            ]
        return []

    @property
    def get_legend_type(self) -> str | None:
        return (
            None
            if self.load.get("legend") is None
            else self.load.get("legend").get("type")
        )

    @property
    def get_legend_icons_as_md(self):
        icons = self.get_legend_icons
        res = [f"`{i.name}` {i.icon}" for i in icons]
        return "" if res == [] else "**legend_icons**\n" + "\n".join(res)
