from zero_to_one_hundred.src.zero_to_one_hundred.configs.sb_config_map import (
    SAFARI_BOOKS_MAP,
    SBConfigMap,
)
from zero_to_one_hundred.src.zero_to_one_hundred.factories.a_factory_provider import (
    AFactoryProvider,
)
from zero_to_one_hundred.src.zero_to_one_hundred.factories.sb_factory import SBFactory
from zero_to_one_hundred.src.zero_to_one_hundred.repository.sb_persist_fs import (
    SBPersistFS,
)


class SBFactoryProvider(AFactoryProvider):
    """SBFactoryProvider"""

    def __init__(self, persist_fs: SBPersistFS):
        super().__init__(persist_fs)
        self.persist_fs = persist_fs

    def provide(self) -> SBFactory:
        config_map = SBConfigMap(self.persist_fs)
        config_map_type = config_map.get_type
        if config_map_type == SAFARI_BOOKS_MAP:
            return SBFactory(config_map, self.persist_fs)
        raise NotImplementedError(
            f"Expected {config_map_type}, check the files contents of {config_map}"
        )
