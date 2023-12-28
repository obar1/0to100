from zero_to_one_hundred.models.readme_md import ReadMeMD
from zero_to_one_hundred.models.section import Section
from zero_to_one_hundred.repository.persist_fs import PersistFS
from zero_to_one_hundred.repository.process_fs import ProcessFS


def test_refresh_links(get_config_map, http_url):
    ReadMeMD(get_config_map, PersistFS, ProcessFS, Section.from_dir_to_http_url, http_url)
