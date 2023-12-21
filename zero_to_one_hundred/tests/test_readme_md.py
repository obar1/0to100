from zero_to_one_hundred.models.readme_md import ReadMeMD
from zero_to_one_hundred.models.section import Section
from zero_to_one_hundred.tests.moke import persist_fs_fake, process_fs_fake


def test_refresh_links(get_config_map, http_url):
    section = Section(persist_fs_fake, process_fs_fake, get_config_map, http_url)
    ReadMeMD(
        persist_fs_fake,
        process_fs_fake,
        get_config_map,
        section.dir_name,
        section.http_url,
    )
