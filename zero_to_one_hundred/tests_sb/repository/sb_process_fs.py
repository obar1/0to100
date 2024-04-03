from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.tests.repository.ztoh_process_fs import ZTOHProcessFS


class SBProcessFS(ZTOHProcessFS):
    @classmethod
    def write_img(cls, path_img, http_url_img):
        pass

    @classmethod
    def write_epub(cls, config_map: SBConfigMap, path_epub, isbn):
        pass
