from zero_to_one_hundred.repository.persist_fs import PersistFS
from zero_to_one_hundred.repository.process_fs import ProcessFS
from zero_to_one_hundred.factories.a_factory_provider import AFactoryProvider
from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.configs.ztoh_config_map import ZTOH_MAP, ZTOHConfigMap


class ZTOHFactoryProvider(AFactoryProvider):
    """0to100 FactoryProvider."""

    def __init__(self, persist_fs: PersistFS, process_fs: ProcessFS):
        super().__init__(persist_fs, process_fs)
        self.persist_fs = persist_fs
        self.process_fs = process_fs

    def provide(self) -> ZTOHFactory:
        config_map = ZTOHConfigMap(self.persist_fs)
        config_map_type = config_map.get_type
        if config_map_type == ZTOH_MAP:
            return ZTOHFactory(config_map, self.persist_fs, self.process_fs)
        raise NotImplementedError(f"NotImplementedError {config_map_type}")
