"""Factory provider."""


# pylint: disable=R0903,E0401,W0703
import logging
import os

from configs.config_loader import ConfigLoader
from factories.ztoh_factory import ZTOHFactory
from validator.validator import is_valid_http


class FactoryProvider:
    """FactoryProvider class.

    Provides factory implementation.
    """

    def __init__(self, args):
        self.__args = args

    def provide(self) -> ZTOHFactory:
        """The method returns instance of MSEFactory."""
        config_file = os.getenv("CONFIG_FILE")
        assert config_file is not None

        config = ConfigLoader(config_file).load()

        logging.info("Loading config: config %s.", config_file)

        http = self.__args[1]
        assert is_valid_http(http)
        return ZTOHFactory(config, http)
