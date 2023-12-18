from zero_to_one_hundred.models.readme_md import ReadMeMD
from zero_to_one_hundred.models.section import Section
from zero_to_one_hundred.repository.persist_fs import PersistFS as persist_fs
from zero_to_one_hundred.tests.moke.process_fs_fake import ProcessFSFake as process_fs


def test_refresh_links(get_config_map, http_url):
    section = Section(persist_fs, process_fs, get_config_map, http_url)
    ReadMeMD(persist_fs, process_fs, get_config_map, section.dir_name, section.http_url)
