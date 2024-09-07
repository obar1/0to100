import logging
from typing import List

from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.models.meta_book import MetaBook
from zero_to_one_hundred.repository.sb_persist_fs import SBPersistFS
from zero_to_one_hundred.views.markdown_renderer import MarkdownRenderer


class Toc(MarkdownRenderer):
    """Toc:
    toc md with list of meta_book as found in fs
    """

    def __init__(
        self,
        config_map: SBConfigMap,
        persist_fs: SBPersistFS,
        process_fs,
        meta_books: List[MetaBook],
    ):
        self.config_map = config_map
        self.readme_md = "toc.md"
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.meta_books = meta_books

    def __repr__(self):
        return f"Toc {self.readme_md}, {str(self.meta_books)}"

    @classmethod
    def build_from_dirs(
        cls, config_map, persist_fs, process_fs, dirs: List[str]
    ) -> List[MetaBook]:
        """from a list of dirs created return the a MetaBook
        m> org http is lost
        """
        res = [
            MetaBook.build_from_dir(config_map, persist_fs, process_fs, curr_dir)
            for curr_dir in dirs
            if curr_dir is not None
        ]
        logging.info(res)
        return res

    def asMarkDown(self):
        def flatten_meta_book(meta_book: MetaBook):
            logging.info(f"flatten_meta_book {meta_book}")
            txt = "|".join(
                [
                    f'<span style="color:blue">**{meta_book.isbn}**</span>',
                    f"![`img`]({meta_book.path_img_as_md})",
                    f"[`xyz`]({meta_book.contents_path_as_md})",
                    f"{meta_book.metadata.as_mark_down()}",
                    f"{meta_book.metadata.status}",
                ]
            )

            return "|" + txt + "|"

        flattened_meta_book = [flatten_meta_book(mb) for mb in self.meta_books]
        backslash_n_char = "\n"

        md = []
        md.append(
            f"""
# TOC
## `{len(self.meta_books)}` metabook
### {self.process_fs.get_now()}
|  ISBN 	|   img	|  `meta-contents`  	|  `json-contents` 	| `status` |
|---	|---	|---	|---		|---	|
{backslash_n_char.join(flattened_meta_book)}
        """
        )
        return md

    def write(self):
        md = self.asMarkDown()
        return self.persist_fs.write_file(self.readme_md, md)
