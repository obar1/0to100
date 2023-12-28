# pylint: disable=W0621,W0613

import pytest

from zero_to_one_hundred.configs.sb_config_map import SAFARI_BOOKS
from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.factories.sb_factory_provider import SBFactoryProvider
from zero_to_one_hundred.repository.sb_persist_fs import SBPersistFS as sb_persist_fs
from zero_to_one_hundred.repository.sb_process_fs import SBProcessFS as sb_process_fs


@pytest.fixture
def get_factory_provider(mock_settings_env_vars):
    return SBFactoryProvider(sb_persist_fs, sb_process_fs)


def test_provide__pass(get_factory_provider):
    actual: SBConfigMap = get_factory_provider.provide().config_map
    assert actual.get_type == SAFARI_BOOKS
    assert actual.get_books_path is not None
    assert actual.get_download_engine_books_path is not None
    assert actual.get_oreilly_username is not None
    assert actual.get_oreilly_userpassword is not None
    assert actual.get_oreilly_userpassword is not None
    assert actual.get_split_pdf_pages == 100
