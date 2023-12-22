from typing import List

from zero_to_one_hundred.configs.config_map import ConfigMap
from zero_to_one_hundred.models.map import Map
from zero_to_one_hundred.models.section import Section
from zero_to_one_hundred.processors.a_processor import AProcessor


class RefreshLinksProcessor(AProcessor):
    """RefreshLinksProcessor:
    in each md there are links to https://
    when some of them are added as new_section
    replace them with the location of the new_section ..."""

    def __init__(self, persist_fs, process_fs, config_map: ConfigMap):
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.process_fs = process_fs

    def process(self):
        """Scan sections an update links."""
        sections: List[Section] = Map.build_from_dirs(
            self.persist_fs,
            self.process_fs,
            self.config_map,
            self.persist_fs.list_dirs(self.config_map.get_repo_path),
        )
        for s in sections:
            try:
                s.refresh_links()
            except:
                print(f"issue with {s}")
