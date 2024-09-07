import logging

from zero_to_one_hundred.configs.a_config_map import AConfigMap
from zero_to_one_hundred.processors.a_processor import AProcessor
from zero_to_one_hundred.repository.a_persist_fs import APersistFS


class HelpProcessor(AProcessor):
    def __init__(
        self, config_map: AConfigMap, persist_fs: APersistFS, supported_processor
    ):
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.supported_processor = supported_processor

    def process(self):
        logging.info(self.persist_fs.get_pkg_info())
        logging.info(f"{repr(self.config_map)}")
        logging.info([p.name for p in self.supported_processor])
