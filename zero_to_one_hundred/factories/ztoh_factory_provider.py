from zero_to_one_hundred.configs.ztoh_config_map import ZTOH_MAP, ZTOHConfigMap
from zero_to_one_hundred.factories.a_factory_provider import AFactoryProvider
from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS
from zero_to_one_hundred.repository.ztoh_process_fs import ZTOHProcessFS


class ZTOHFactoryProvider(AFactoryProvider):
    """0to100 FactoryProvider."""

    def __init__(self, persist_fs: ZTOHPersistFS, process_fs: ZTOHProcessFS):
        super().__init__(persist_fs, process_fs)
        self.persist_fs = persist_fs
        self.process_fs = process_fs

    def provide(self) -> ZTOHFactory:
        config_map = ZTOHConfigMap(self.persist_fs)
        config_map_type = config_map.get_type
        if config_map_type == ZTOH_MAP:
            return ZTOHFactory(config_map, self.persist_fs, self.process_fs)
        raise NotImplementedError(
            f"Expected {config_map_type}, check the files contents of {config_map}"
        )
