# pylint: disable=W0621,W0613

import pytest
from zero_to_one_hundred.configs.sb_config_map import SAFARI_BOOKS

from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.factories.sb_factory_provider import SBFactoryProvider
from zero_to_one_hundred.repository.persist_fs import PersistFS as persist_fs
from zero_to_one_hundred.tests.moke import process_fs_fake


@pytest.fixture
def get_factory_provider(mock_settings_env_vars):
    return SBFactoryProvider(persist_fs, process_fs_fake)


def test_provide__pass(get_factory_provider):
    actual: SBConfigMap = get_factory_provider.provide().config_map
    assert actual.get_type == SAFARI_BOOKS
    assert actual.get_books_path is not None
    assert actual.get_download_engine_books_path is not None
    assert actual.get_oreilly_username is not None
    assert actual.get_oreilly_userpassword is not None
