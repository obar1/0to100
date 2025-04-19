class YTConfigMap:
    """YTConfigMap class to handle YouTube-specific configurations."""

    def __init__(self, video_url: str, download_path: str):
        self.video_url = video_url
        self.download_path = download_path

    def get_video_url(self):
        return self.video_url

    def get_download_path(self):
        return self.download_path
