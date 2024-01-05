from zero_to_one_hundred.models.readme_md import ReadMeMD
from zero_to_one_hundred.models.section import Section


def test_refresh_links(get_config_map, persist_fs, process_fs, http_url):
    ReadMeMD(
        get_config_map,
        persist_fs,
        process_fs,
        Section.from_http_url_to_dir,
        http_url,
    )
