from zero_to_one_hundred.configs.sb_config_map import SAFARI_BOOKS_MAP, SBConfigMap
from zero_to_one_hundred.exceptions.errors import UnsupportedConfigMapError
from zero_to_one_hundred.factories.a_factory_provider import AFactoryProvider
from zero_to_one_hundred.factories.sb_factory import SBFactory
from zero_to_one_hundred.repository.sb_persist_fs import SBPersistFS
from zero_to_one_hundred.repository.sb_process_fs import SBProcessFS


class SBFactoryProvider(AFactoryProvider):
    """SBFactoryProvider"""

    def __init__(self, persist_fs: SBPersistFS, process_fs: SBProcessFS):
        super().__init__(persist_fs, process_fs)
        self.persist_fs = persist_fs
        self.process_fs = process_fs

    def provide(self) -> SBFactory:
        config_map = SBConfigMap(self.persist_fs)
        config_map_type = config_map.get_type
        if config_map_type == SAFARI_BOOKS_MAP:
            return SBFactory(config_map, self.persist_fs, self.process_fs)
        raise UnsupportedConfigMapError(config_map_type)
