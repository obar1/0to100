"""Factory provider."""


# pylint: disable=R0903,E0401,W0703
import logging
import os

from configs.config import Config
from configs.config_loader import ConfigLoader
from factories.ztoh_factory import ZTOHFactory
from validator.validator import is_valid_http

CONFIG_FILE = "CONFIG_FILE"


class FactoryProvider:
    """FactoryProvider class.

    Provides factory implementation.
    """

    def __init__(self, args):
        self.__args = args
        self.__config_file = os.getenv(CONFIG_FILE)

    def provide(self) -> ZTOHFactory:
        """The method returns instance of MSEFactory."""
        logging.info("Loading config: config %s.", self.__config_file)
        config: Config = ConfigLoader(self.__config_file).load()
        logging.info("Config: %s.", config)

        return ZTOHFactory(config, self.__args)
