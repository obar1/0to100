"""ZTOHFactory."""


# pylint: disable=R0903,E0401,W0703,W1201

from configs.config import Config
from processors.section_processor import SectionProcessor
from repository.repository import Persist


class ZTOHFactory:
    """ZTOHFactory class."""

    def __init__(self, config: Config, http_url: str):
        """Constructor.

        Args:
            http_url: url to prpcess
            config: yaml path
        """
        self.__config = config
        self.__http_url = http_url
        self.__persist = Persist(config)

    def create_section_processor(self):
        """Creates necessary resource for Ingestion CF."""
        return SectionProcessor(self.__config, self.__http_url, self.__persist)
