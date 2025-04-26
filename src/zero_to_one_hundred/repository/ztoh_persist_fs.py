# pylint: disable=W0108
import logging
import os
import time
from yt_dlp import YoutubeDL

from src.zero_to_one_hundred.repository.a_persist_fs import (
    APersistFS,
)
from src.zero_to_one_hundred.validator.validator import Validator


class ZTOHPersistFS(APersistFS):
    """ZTOHPersistFS:
    deal with FS
    """

    @classmethod
    def done_section(cls, path):
        path = cls.abs_path(path)
        logging.debug(f"done_section {path}")
        path = path + os.sep + ".done"
        logging.debug(f"path {path}")
        os.makedirs(path, 0o777, True)
        with open("{}/.gitkeep".format(path), "a", encoding="utf-8"):
            os.utime("{}/.gitkeep".format(path), None)
        logging.debug(f"created {path}")

    @classmethod
    def done_section_status(cls, abs_repo_path, path):
        logging.debug(f"done_section_status {path}")
        path = abs_repo_path + os.sep + path + os.sep + ".done"
        logging.debug(f"path {path}")
        exists = os.path.exists(path)
        if exists:
            return True
        return False

    @classmethod
    def get_biz_ts(cls, path):
        logging.debug(f"path {path}")
        exists = os.path.exists(path)

        if exists:
            res = os.path.getmtime(path)
            return res
        return time.time()

    @classmethod
    def path_as_md(cls, a_path):
        """
        use relative path and convert " " to %20
        """
        return a_path.replace(" ", "%20")

    @classmethod
    def snatch_yt_video(cls, video_url, full_dir_name, readme_md, txt):
        @staticmethod
        def download_youtube_video(url, output_path):
            """Download a YouTube video as MP4 and return video info including tags and subtitles."""

            # Configure yt-dlp options for browser-compatible MP4 and subtitles
            ydl_opts = {
                "format": 'bestvideo[vcodec~="^avc1"][ext=mp4]+bestaudio[acodec~="mp4a"]/best[ext=mp4]',  # H.264 + AAC
                "outtmpl": os.path.join(output_path, "%(title)s.%(ext)s"),
                "merge_output_format": "mp4",
                "postprocessors": [
                    {
                        "key": "FFmpegVideoConvertor",
                        "preferedformat": "mp4",  # Ensure MP4 with H.264/AAC
                    }
                ],
                "writesubtitles": True,  # Download subtitles if available
                "writeautomaticsub": True,  # Download automatic subtitles
                "subtitleslangs": ["en"],  # Prefer English subtitles
                "subtitlesformat": "vtt",  # WebVTT format for browser compatibility
            }

            # Download the video
            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                video_title = info.get("title", "Untitled Video")
                raw_filename = ydl.prepare_filename(info).split(os.sep)[-1]
                video_filename = raw_filename

                # Get tags
                tags = info.get("tags", []) or []
                if not tags:
                    tags = ["No tags available"]

                # Get subtitles
                subtitles = None
                subtitle_file = os.path.join(
                    output_path,
                    f"{(info.get('title', 'video'))}.en.vtt",
                )
                if os.path.exists(subtitle_file):
                    with open(subtitle_file, "r", encoding="utf-8") as f:
                        subtitles = f.read()
                else:
                    subtitles = "No subtitles available"

                logging.debug(f"Downloading: {video_title}")
                logging.debug(f"Download completed! Video saved to {output_path}")
                return {
                    "title": video_title,
                    "filename": video_filename,
                    "path": os.path.join(output_path, video_filename),
                    "tags": tags,
                    "subtitles": subtitles,
                }

        try:
            cls.make_dirs(full_dir_name)

            video_info = download_youtube_video(video_url, full_dir_name)

            txt.append(f"# {video_info.get('title')}")
            txt.append("\n")
            txt.append(
                f"[{video_info.get('filename')}]({cls.path_as_md(video_info.get('filename'))})"
            )
            txt.append("\n")

            txt.append(f"tags `{video_info.get('tags')}`")
            txt.append("\n")

        except Exception as e:
            Validator.print_e(e)
        cls.write_file(readme_md, txt)
