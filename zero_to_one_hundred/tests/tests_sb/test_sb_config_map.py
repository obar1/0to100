from zero_to_one_hundred.configs.sb_config_map import SAFARI_BOOKS_MAP, SBConfigMap


# pylint: disable=W0621,W0613


def test_provide__pass(get_config_map: SBConfigMap):
    actual = get_config_map
    assert actual.get_type == SAFARI_BOOKS_MAP
    assert actual.get_books_path is not None
    assert actual.get_download_engine_books_path is not None
    assert actual.get_oreilly_username is not None
    assert actual.get_oreilly_userpassword is not None
    assert actual.get_oreilly_userpassword is not None
    assert actual.get_split_pdf_pages == 0
    assert actual.get_download_books is False
