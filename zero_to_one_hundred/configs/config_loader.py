"""TODO."""
import logging

import yaml

from configs.config import Config


# pylint: disable=R0903,E0401,W0703,W1514
class ConfigLoader:
    """TODO."""

    def __init__(self, config_file):
        """Constructor."""
        self._config_file = config_file
        self._config = None

    def load(self) -> Config:
        """Main load method."""
        with open(self._config_file, "r") as stream:
            logging.info("Start loading config file %s", self._config_file)
            config = yaml.safe_load(stream)
            logging.info("Config file %s is loaded successfully.", self._config_file)
            return Config(config)
