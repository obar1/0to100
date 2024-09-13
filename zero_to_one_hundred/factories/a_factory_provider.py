from zero_to_one_hundred.factories.a_factory import AFactory


class AFactoryProvider:
    """AFactoryProvider."""

    def __init__(self, persist_fs=None, process_fs=None):
        self.persist_fs = persist_fs
        self.process_fs = process_fs

    def provide(self) -> None | AFactory:
        return AFactory(persist_fs=self.persist_fs)
