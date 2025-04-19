from zero_to_one_hundred.src.zero_to_one_hundred.configs.yt_config_map import (
    YTConfigMap,
)
from zero_to_one_hundred.src.zero_to_one_hundred.processors.yt_download_processor import (
    YTDownloadProcessor,
)


class YTFactory:
    """YTFactory class."""

    def __init__(self, config_map: YTConfigMap):
        self.config_map = config_map

    def get_processor(self):
        return YTDownloadProcessor(
            self.config_map.get_video_url(), self.config_map.get_download_path()
        )
