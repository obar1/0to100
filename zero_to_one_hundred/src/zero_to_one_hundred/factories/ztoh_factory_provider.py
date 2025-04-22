from zero_to_one_hundred.src.zero_to_one_hundred.configs.ztoh_config_map import (
    ZTOH_MAP,
    ZTOHConfigMap,
)
from zero_to_one_hundred.src.zero_to_one_hundred.factories.a_factory_provider import (
    AFactoryProvider,
)
from zero_to_one_hundred.src.zero_to_one_hundred.factories.ztoh_factory import (
    ZTOHFactory,
)
from zero_to_one_hundred.src.zero_to_one_hundred.repository.ztoh_persist_fs import (
    ZTOHPersistFS,
)



class ZTOHFactoryProvider(AFactoryProvider):
    """0to100 FactoryProvider."""

    def __init__(self, persist_fs: ZTOHPersistFS):
        super().__init__(persist_fs)
        self.persist_fs = persist_fs

    def provide(self) -> ZTOHFactory:
        config_map = ZTOHConfigMap(self.persist_fs)
        config_map_type = config_map.get_type
        if config_map_type == ZTOH_MAP:
            return ZTOHFactory(config_map, self.persist_fs)
        raise NotImplementedError(
            f"Expected {config_map_type}, check the files contents of {config_map}"
        )
