"""RefreshMapProcessor:
refresh sections in map
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging
import os

VERSION = "__version__ = "

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root


class HelpProcessor:
    """HelpProcessor"""

    def __init__(self, persist_fs, supported_processor):
        """init"""
        self.supported_processor = supported_processor
        self.persist_fs = persist_fs

    @property
    def get_version(self):
        """read file and return the version"""
        change_log_relative_path = "../../changelog.md"
        change_log_path = self.persist_fs.abs_path(
            os.path.join(ROOT_DIR, change_log_relative_path)
        )
        try:
            with open(change_log_path, mode="r", encoding="UTF-8") as file_change_log:
                txt = file_change_log.readlines()
                version = max(sorted(filter(lambda f: VERSION in f, txt)))
                logging.debug(f"v. {version}")
                return version.strip()
        except FileNotFoundError:
            logging.exception(f"not found {change_log_path}")
        except:
            logging.exception(f"check contents {change_log_path}")
        return None

    def process(self):
        """Get version."""
        logging.debug(self.supported_processor)
        return self.get_version
