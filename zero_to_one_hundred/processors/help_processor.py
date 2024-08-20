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
        print(self.persist_fs.get_pkg_info())
        print(f"{repr(self.config_map)}")
        print([p.name for p in self.supported_processor])
