"""ZTOHFactory."""


# pylint: disable=R0903,E0401,W0703

from configs.config import Config
from processors.section_processor import SectionProcessor


class ZTOHFactory:
    """ZTOHFactory class."""

    def __init__(self, config: Config):
        """Constructor."""
        self.__config = config

        print(self.__config)

    def create_section_processor(self):
        """Creates necessary resource for Ingestion CF."""
        return SectionProcessor(self.__config)
