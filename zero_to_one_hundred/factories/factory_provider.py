"""FactoryProvider:
"""
# pylint: disable=R0903,E0401,W0703

import logging
import os

from configs.config import Config, ConfigMap
from factories.ztoh_factory import ZTOHFactory

CONFIG_FILE = "CONFIG_FILE"


class FactoryProvider:
    """FactoryProvider class.
    Provides factory implementation.
    """

    def __init__(self, PersistFS):
        self.config_file = os.getenv(CONFIG_FILE)
        self.PersistFS=PersistFS

    def provide(self) -> ZTOHFactory:
        """T The method returns instance of MSEFactory."""
        get_type = Config(self.config_file, self.PersistFS).get_type
        if get_type == 'map':
            config_map = ConfigMap(self.config_file, self.PersistFS)
            return ZTOHFactory(config_map, self.PersistFS)
        else:
            raise NotImplementedError(f'NotImplementedError {get_type}')
