import pathlib

import fitz


from src.zero_to_one_hundred.processors.pdf_to_md_inline_processor import (
    PdfToMdInlineProcessor,
)


def create_sample_pdf(path: pathlib.Path, text: str = "Hello PDF"):
    """Create a tiny one-page PDF with the given text using PyMuPDF."""
    doc = fitz.open()
    page = doc.new_page()
    # Insert text at a modest offset
    page.insert_text((72, 72), text)
    doc.save(str(path))


def test_pdf_to_md_inline_processor_creates_md(tmp_path, get_config_map, persist_fs):
    pdf_path = tmp_path / "sample.pdf"
    md_path = tmp_path / "sample.md"

    create_sample_pdf(pdf_path, text="This is a test PDF")

    proc = PdfToMdInlineProcessor(
        get_config_map, persist_fs, str(pdf_path), str(md_path)
    )
    proc.process()

    # Assert md file is created and contains the PDF stem as a heading
    assert md_path.exists()
    content = md_path.read_text(encoding="utf-8")
    assert f"# {pdf_path.stem}" in content
    # Since we inserted text, the extracted text (or fallback) should appear
    assert "This is a test PDF" in content
