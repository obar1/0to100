from unittest.mock import patch
from zero_to_one_hundred.processors.yt_download_processor import YTDownloadProcessor


def test_yt_download_processor():
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    download_path = "/tmp"

    with patch("pytube.YouTube") as MockYouTube:
        mock_stream = (
            MockYouTube.return_value.streams.get_highest_resolution.return_value
        )
        mock_stream.download.return_value = None

        processor = YTDownloadProcessor(video_url, download_path)
        processor.process()

        MockYouTube.assert_called_once_with(video_url)
        mock_stream.download.assert_called_once_with(output_path=download_path)
