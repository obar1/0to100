"""FactoryProvider:
provides the actual factory based on the type value
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203


from zero_to_one_hundred.configs.config import Config
from zero_to_one_hundred.configs.sb_config_map import SAFARI_BOOKS, SBConfigMap
from zero_to_one_hundred.exceptions.errors import UnsupportedConfigMap
from zero_to_one_hundred.factories.factory_provider import FactoryProvider
from zero_to_one_hundred.factories.sb_factory import SBFactory


class SBFactoryProvider(FactoryProvider):
    def provide(self) -> SBFactory:
        """T The method returns instance of MSEFactory."""
        get_type = Config(self.MAP_YAML_PATH, self.persist_fs).get_type
        if get_type == SAFARI_BOOKS:
            config_map = SBConfigMap(self.MAP_YAML_PATH, self.persist_fs)
            return SBFactory(config_map, self.persist_fs, self.process_fs)
        raise UnsupportedConfigMap(get_type)
