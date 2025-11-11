from enum import Enum

from src.zero_to_one_hundred.configs.ztoh_config_map import (
    ZTOHConfigMap,
)
from src.zero_to_one_hundred.factories.a_factory import AFactory, UV_RUN_MAIN
from src.zero_to_one_hundred.processors.create_section_processor import (
    CreateSectionProcessor,
)
from src.zero_to_one_hundred.processors.done_section_processor import (
    DoneSectionProcessor,
)
from src.zero_to_one_hundred.processors.refresh_map_processor import (
    RefreshMapProcessor,
)
from src.zero_to_one_hundred.processors.refresh_section_contents_processor import (
    RefreshSectionContentsProcessor,
)
from src.zero_to_one_hundred.processors.pdf_to_md_inline_processor import (
    PdfToMdInlineProcessor,
)
from src.zero_to_one_hundred.repository.ztoh_persist_fs import (
    ZTOHPersistFS,
)
from src.zero_to_one_hundred.validator.validator import Validator


class ZTOHFactory(AFactory):
    """0to100 Factory class."""

    class SUPPORTED_PROCESSOR(Enum):
        create_section = 1
        done_section = 2
        refresh_map = 3
        refresh_section_contents = 4
        pdf_to_md = 5
        help = 6

    extended_help = f"""
    create_section = create a new section
    section=https://www.cloudskillsboost.google/paths/16
    {UV_RUN_MAIN} zo create_section "$section"

    done_section = tag a section as done
    section=https://www.cloudskillsboost.google/paths/16
    {UV_RUN_MAIN} zo done_section "$section"

    refresh_map = refresh the section map
    {UV_RUN_MAIN} zo refresh_map

    refresh_section_contents = refresh links to sections in the readme.md(s)
    {UV_RUN_MAIN} zo refresh_section_contents

    pdf_to_md = convert a PDF to a single Markdown file with inline images
    {UV_RUN_MAIN} zo pdf_to_md "/path/to/input.pdf" "/path/to/output.md"
    """

    def __init__(
        self,
        config_map: ZTOHConfigMap,
        persist_fs: ZTOHPersistFS,
    ):
        super().__init__(persist_fs=persist_fs)
        self.config_map = config_map

    def get_processor(self, args):
        cmd, p1, p2, _ = Validator.validate_args(args)
        if cmd == ZTOHFactory.SUPPORTED_PROCESSOR.create_section.name:
            yield self.create_section_processor(p1)
            yield self.refresh_map_processor()
        elif cmd == ZTOHFactory.SUPPORTED_PROCESSOR.done_section.name:
            yield self.done_section_processor(p1)
            yield self.refresh_map_processor()
        elif cmd == ZTOHFactory.SUPPORTED_PROCESSOR.refresh_map.name:
            yield self.refresh_map_processor()
        elif cmd == ZTOHFactory.SUPPORTED_PROCESSOR.refresh_section_contents.name:
            yield self.refresh_section_contents_processor()
            yield self.refresh_map_processor()
        elif cmd == ZTOHFactory.SUPPORTED_PROCESSOR.pdf_to_md.name:
            yield self.pdf_to_md_processor(p1, p2)
        elif cmd == ZTOHFactory.SUPPORTED_PROCESSOR.help.name:
            yield self.help_processor()
        else:
            yield self.unsupported_processor(cmd, self.SUPPORTED_PROCESSOR)

    def create_section_processor(self, http_url):
        return CreateSectionProcessor(self.config_map, self.persist_fs, http_url)

    def done_section_processor(self, http_url):
        return DoneSectionProcessor(self.config_map, self.persist_fs, http_url)

    def refresh_map_processor(self):
        return RefreshMapProcessor(self.config_map, self.persist_fs)

    def refresh_section_contents_processor(self):
        return RefreshSectionContentsProcessor(self.config_map, self.persist_fs)

    def pdf_to_md_processor(self, pdf_path, md_path=None):
        return PdfToMdInlineProcessor(
            self.config_map, self.persist_fs, pdf_path, md_path
        )
