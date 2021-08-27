"""Factory provider."""


# pylint: disable=R0903,E0401,W0703
import logging
import os

from configs.config_loader import ConfigLoader
from factories.ztoh_factory import ZTOHFactory


class FactoryProvider:
    """FactoryProvider class.

    Provides factory implementation.
    """

    @classmethod
    def provide(cls) -> ZTOHFactory:
        """The method returns instance of MSEFactory."""
        config_file = os.getenv("CONFIG_FILE")
        assert config_file is not None

        config = ConfigLoader(config_file).load()

        logging.info("Loading config: config %s.", config_file)

        return ZTOHFactory(config)
