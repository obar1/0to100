from zero_to_one_hundred.factories.sb_factory_provider import SBFactoryProvider


# pylint: disable=W0621


def test_pass(get_config_map, persist_fs, process_fs, get_factory):
    actual = SBFactoryProvider(persist_fs, process_fs)
    assert isinstance(actual.provide(), type(get_factory))
