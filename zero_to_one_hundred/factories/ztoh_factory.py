"""ZTOHFactory."""


# pylint: disable=R0903,E0401,W0703,W1201
from typing import List

from configs.config import Config
from processors.refresh_sections_processor import RefreshSectionsProcessor
from processors.create_section_processor import CreateSectionProcessor
from repository.persist_fs import PersistFS


class ZTOHFactory:
    """ZTOHFactory class."""

    def __init__(self, config: Config, args: List[str]):
        """Constructor.

        Args:
            args: url to prpcess
            config: yaml path
        """
        self.__config = config
        self.__args = args
        self.__persist = PersistFS(config)

    def get_processor(self):
        """get the processor """
        cmd=self.__args[1]
        if cmd=="create_section":
            return self.create_section_processor()
        elif cmd == "refresh_sections":
            return self.refresh_sections_processor()
        else:
            raise ValueError(self.__args )

    def create_section_processor(self):
        http_url=self.__args[2]
        return CreateSectionProcessor(self.__config, http_url, self.__persist)

    def refresh_sections_processor(self):
        return RefreshSectionsProcessor(self.__config, self.__persist)
