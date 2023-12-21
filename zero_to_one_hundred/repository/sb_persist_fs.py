"""PersistFS:
deal with FS
mocked in Test
"""

import os
from pathlib import Path
from shutil import copyfile
from typing import List

import yaml

from zero_to_one_hundred.repository.persist_fs import PersistFS

PREFIX_RELATIVE_FOLDER = "./"


class SBPersistFS(PersistFS):
    @classmethod
    def is_relative_path(cls, path):
        if str(path).startswith(PREFIX_RELATIVE_FOLDER):
            return True
        return False

    @classmethod
    def render_json(cls, txt: str):
        return txt.replace('"', ' " ').replace("\n", " <br/> ")

    @classmethod
    def render_path(cls, txt: str):
        return txt.replace(" ", "%20")
