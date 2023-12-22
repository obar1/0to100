from zero_to_one_hundred.configs.a_config_map import AConfigMap
from zero_to_one_hundred.configs.sb_config_map import SAFARI_BOOKS, SBConfigMap
from zero_to_one_hundred.exceptions.errors import UnsupportedConfigMapError
from zero_to_one_hundred.factories.a_factory_provider import AFactoryProvider
from zero_to_one_hundred.factories.sb_factory import SBFactory


class SBFactoryProvider(AFactoryProvider):
    """SBFactoryProvider class."""

    def provide(self) -> SBFactory:
        """T The method returns instance of MSEFactory."""
        get_type = AConfigMap(self.MAP_YAML_PATH, self.persist_fs).get_type
        if get_type == SAFARI_BOOKS:
            config_map = SBConfigMap(self.MAP_YAML_PATH, self.persist_fs)
            return SBFactory(config_map, self.persist_fs, self.process_fs)
        raise UnsupportedConfigMapError(get_type)
