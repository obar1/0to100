from typing import List
from connect.utils.terminal.markdown import render

from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.models.meta_book import MetaBook


class Toc:
    """Toc:
    toc md with list of meta_book as found in fs
    """

    def __init__(
        self,
        config_map: SBConfigMap,
        persist_fs,
        process_fs,
        meta_books: List[MetaBook],
    ):
        self.config_map = config_map
        self.readme_md = "toc.md"
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.meta_books = meta_books

    def __repr__(self):
        return f"Toc {self.readme_md}, {self.meta_books}"

    def __repr_flatten(self, meta_books: List[MetaBook]) -> str:
        """transform as
        1. <0596007124> ![`img`](../books/0596007124/0596007124.png) :o: [`pdf`](../books/0596007124/0596007124.pdf) :o: [`epub`](../books/0596007124/0596007124.epub) :o: [`json`](../books/0596007124/0596007124.json)
        """

        def flatten_meta_book(s):
            json = self.persist_fs.render_json(s.read_json())
            status = (
                '<span style="color:green">**DONE**</span>'
                if "STATUS_DONE" in json
                else '<span style="color:yellow">**WIP**</span>'
            )
            res = "|".join(
                [
                    f'<span style="color:blue">**{s.isbn}**</span>',
                    f"![`img`]({self.persist_fs.render_path(s.path_img)})",
                    f"[`epub`]({self.persist_fs.render_path(s.path_epub)})",
                    f"[`pdf`]({self.persist_fs.render_path(s.path_pdf)})",
                    f"{json}",
                    f"{status}",
                ]
            )
            return res

        flattened_meta_book = [flatten_meta_book(mb) for mb in meta_books]
        return "\n".join(flattened_meta_book)

    @classmethod
    def build_from_dirs(
        cls, config_map, persist_fs, process_fs, dirs: List[str]
    ) -> List[MetaBook]:
        """from a list of dirs created return the a MetaBook
        m> org http is lost
        """
        return [
            MetaBook.build_from_dir(config_map, persist_fs, process_fs, curr_dir)
            for curr_dir in dirs
            if curr_dir is not None
        ]

    def write(self):
        """write as

        # ./books/toc.md

        table
        """
        txt = []
        txt.append(
            f"""
# TOC
## `{len(self.meta_books)}` books
### {self.process_fs.get_now()}
|  ISBN 	|   	|   	|   	|  `json-contents` 	| `status` |
|---	|---	|---	|---	|---	|---	|
{self.__repr_flatten(self.meta_books)}
        """
        )
        print(render("\n".join(txt)))
        return self.persist_fs.write_file(self.readme_md, txt)
