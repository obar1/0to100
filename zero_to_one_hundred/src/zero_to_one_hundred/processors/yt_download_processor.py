from pytube import YouTube
from zero_to_one_hundred.src.zero_to_one_hundred.processors.a_processor import (
    AProcessor,
)


class YTDownloadProcessor(AProcessor):
    """YTDownloadProcessor:
    Downloads a YouTube video locally."""

    def __init__(self, video_url: str, download_path: str):
        self.video_url = video_url
        self.download_path = download_path

    def process(self):
        """Download the YouTube video to the specified path."""
        try:
            yt = YouTube(self.video_url)
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path=self.download_path)
            print(f"Downloaded: {yt.title} to {self.download_path}")
        except Exception as e:
            print(f"Failed to download video: {e}")
