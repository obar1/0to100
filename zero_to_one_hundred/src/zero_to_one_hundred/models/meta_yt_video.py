from yt_dlp import YoutubeDL
import os
import json
import html
import re
import logging
import os
import re

from zero_to_one_hundred.src.zero_to_one_hundred.models.section import Section
from zero_to_one_hundred.src.zero_to_one_hundred.repository.yt_persist_fs import (
    YTPersistFS,
)
from zero_to_one_hundred.src.zero_to_one_hundred.views.markdown_renderer import (
    MarkdownRenderer,
)


from zero_to_one_hundred.src.zero_to_one_hundred.configs.ztoh_config_map import (
    ZTOHConfigMap,
)
from zero_to_one_hundred.src.zero_to_one_hundred.models.readme_md import ReadMeMD
from zero_to_one_hundred.src.zero_to_one_hundred.repository.ztoh_persist_fs import (
    ZTOHPersistFS,
)
from zero_to_one_hundred.src.zero_to_one_hundred.repository.ztoh_process_fs import (
    ZTOHProcessFS,
)
from zero_to_one_hundred.src.zero_to_one_hundred.validator.validator import Validator
from zero_to_one_hundred.src.zero_to_one_hundred.views.markdown_renderer import (
    MarkdownRenderer,
)


class MetaYTVideo(Section):
    """
    MetaYTVideo
    """

    # Directory to store videos
    VIDEO_DIR = "videos"
    # JSON file to track downloaded videos
    VIDEO_DB = "videos.json"
    # HTML file for the webpage
    INDEX_HTML = "index.html"

    def __init__(
        self,
        config_map: ZTOHConfigMap,
        persist_fs: YTPersistFS,
        process_fs: ZTOHProcessFS,
        yt_url: str,
        is_done: bool = False,
    ):
        super().__init__(config_map, persist_fs, process_fs, yt_url, is_done)

    def __repr__(self):
        return f"MetaYTVideo {self.yt_url} {self.dir_readme_md} {self.is_done} {self.dir_name}"

    def write(self, txt: str):
        return self.persist_fs.snatch_yt_video(
            self.yt_url, self.dir_name, self.dir_readme_md
        )

    def sanitize_filename(filename):
        """Remove or replace invalid characters for filenames."""
        return re.sub(r'[<>:"/\\|?*]', "_", filename)
