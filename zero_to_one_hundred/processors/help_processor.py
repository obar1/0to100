import logging

from zero_to_one_hundred.configs.a_config_map import AConfigMap
from zero_to_one_hundred.processors.a_processor import AProcessor
from zero_to_one_hundred.repository.a_persist_fs import APersistFS


class HelpProcessor(AProcessor):
    def __init__(
        self,
        config_map: AConfigMap,
        persist_fs: APersistFS,
        supported_processor,
        extended_help,
    ):
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.supported_processor = supported_processor
        self.extended_help = extended_help

    def process(self):
        logging.info(self.persist_fs.get_pkg_info())
        if self.config_map:
            logging.info(f"config_map: {repr(self.config_map)}")
        logging.info(f"supported: {[s.name for s in self.supported_processor]}")
        logging.info(f"extended help: {self.extended_help}")
