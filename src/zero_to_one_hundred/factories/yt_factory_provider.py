from zero_to_one_hundred.configs.yt_config_map import (
    YTConfigMap,
)
from zero_to_one_hundred.factories.yt_factory import YTFactory


class YTFactoryProvider:
    """YTFactoryProvider class."""

    def __init__(self, video_url: str, download_path: str):
        self.config_map = YTConfigMap(video_url, download_path)

    def provide(self) -> YTFactory:
        return YTFactory(self.config_map)
