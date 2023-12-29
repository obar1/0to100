from zero_to_one_hundred.configs.a_config_map import AConfigMap

from zero_to_one_hundred.processors.a_processor import AProcessor


class HelpProcessor(AProcessor):
    def __init__(self, config_map: AConfigMap, supported_processor):
        self.config_map = config_map
        self.supported_processor = supported_processor

    def process(self):
        print(f"{self.config_map.__repr__()}")
        print([p.name for p in self.supported_processor])
