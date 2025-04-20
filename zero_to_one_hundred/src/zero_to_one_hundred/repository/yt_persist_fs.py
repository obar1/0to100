import logging
import os
import json
import html
import re
from yt_dlp import YoutubeDL

from zero_to_one_hundred.src.zero_to_one_hundred.repository.ztoh_persist_fs import (
    ZTOHPersistFS,
)


@staticmethod
def sanitize_filename(txt):
    return txt


INDEX_HTML = ""


class YTPersistFS(ZTOHPersistFS):
    """YTPersistFS:
    deal with FS
    """

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
            video_filename = sanitize_filename(raw_filename)

            # Get tags
            tags = info.get("tags", []) or []
            if not tags:
                tags = ["No tags available"]

            # Get subtitles
            subtitles = None
            subtitle_file = os.path.join(
                output_path, f"{sanitize_filename(info.get('title', 'video'))}.en.vtt"
            )
            if os.path.exists(subtitle_file):
                with open(subtitle_file, "r", encoding="utf-8") as f:
                    subtitles = f.read()
            else:
                subtitles = "No subtitles available"

            logging.info(f"Downloading: {video_title}")
            logging.info(f"Download completed! Video saved to {output_path}")
            return {
                "title": video_title,
                "filename": video_filename,
                "path": os.path.join(output_path, video_filename),
                "tags": tags,
                "subtitles": subtitles,
            }

    @staticmethod
    def generate_index_html(video):
        """Generate or update the index.html file with video list, players, tags, and subtitles."""
        html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>YouTube Video Downloads</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            .subtitles { 
                max-height: 200px; 
                overflow-y: auto; 
                background-color: #f8f8f8; 
                padding: 1rem; 
                border-radius: 0.5rem; 
                white-space: pre-wrap;
            }
            .tag { 
                display: inline-block; 
                background-color: #e5e7eb; 
                padding: 0.25rem 0.5rem; 
                border-radius: 0.25rem; 
                margin-right: 0.5rem; 
                margin-bottom: 0.5rem; 
            }
        </style>
    </head>
    <body class="bg-gray-100 font-sans">
        <div class="container mx-auto p-4">
            <h1 class="text-3xl font-bold mb-6 text-center">Downloaded YouTube Videos</h1>
            <div class="grid gap-6">
        """

        escaped_title = html.escape(video["title"])
        video_path = os.path.join(
            "videos", os.path.basename(video["filename"])
        ).replace("\\", "/")
        tags = video.get("tags", ["No tags available"])
        subtitles = html.escape(video.get("subtitles", "No subtitles available"))
        subtitle_track = os.path.join(
            "videos", f"{sanitize_filename(video['title'])}.en.vtt"
        ).replace("\\", "/")

        # Generate tags HTML
        tags_html = "".join(
            f'<span class="tag">{html.escape(tag)}</span>' for tag in tags
        )

        html_content += f"""
            <div class="bg-white p-4 rounded-lg shadow-md">
                <h2 class="text-xl font-semibold mb-2">{escaped_title}</h2>
                <video controls class="w-full max-w-2xl mx-auto rounded" style="aspect-ratio: 16/9;">
                    <source src="{video_path}" type="video/mp4">
                    <track kind="subtitles" src="{subtitle_track}" srclang="en" label="English" default>
                    Your browser does not support the video tag, or the video file may be inaccessible. Ensure the file exists at '{video_path}' and is in a compatible MP4 format (H.264/AAC).
                </video>
                <div class="mt-4">
                    <h3 class="text-lg font-medium mb-2">Tags</h3>
                    <div class="mb-4">{tags_html}</div>
                    <h3 class="text-lg font-medium mb-2">Subtitles</h3>
                    <div class="subtitles">{subtitles}</div>
                </div>
                <a href="{video_path}" class="text-blue-500 hover:underline mt-2 inline-block" download>Download Video</a>
            </div>
    """

        html_content += """
            </div>
        </div>
    </body>
    </html>
    """

        with open(INDEX_HTML, "w") as f:
            f.write(html_content)
        print(f"Updated {INDEX_HTML} with {len(video)} videos.")

    @staticmethod
    def snatch_yt_video(video_url, dir_name, dir_readme_md):
        # Create video directory if it doesn't exist
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        if video_url:
            save_path = dir_name

            # Download the video
            video_info = YTPersistFS.download_youtube_video(video_url, save_path)

            YTPersistFS.generate_index_html(video_info)
