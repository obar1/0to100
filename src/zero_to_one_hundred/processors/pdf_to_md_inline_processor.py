"""Pdf to Markdown processor

Wraps a PDF -> single Markdown-with-inline-images conversion as a Processor.

This file is based on the user's snippet and adapted to the project's
processor pattern (inherit from AProcessor and implement process()).
"""

from __future__ import annotations

import base64
import pathlib
from typing import List, Optional

import fitz  # PyMuPDF

from src.zero_to_one_hundred.processors.a_processor import AProcessor
from src.zero_to_one_hundred.validator.validator import Validator


def _mime_from_ext(ext: str) -> str:
    ext = (ext or "").lower().strip(".")
    if ext in ("jpg", "jpeg"):
        return "image/jpeg"
    if ext == "png":
        return "image/png"
    if ext in ("tif", "tiff"):
        return "image/tiff"
    if ext == "bmp":
        return "image/bmp"
    if ext in ("jp2", "j2k"):
        return "image/jp2"
    if ext == "gif":
        return "image/gif"
    if ext == "webp":
        return "image/webp"
    return "application/octet-stream"


def _to_data_uri(img_bytes: bytes, ext: str) -> str:
    mime = _mime_from_ext(ext)
    b64 = base64.b64encode(img_bytes).decode("ascii")
    return f"data:{mime};base64,{b64}"


class PdfToMdInlineProcessor(AProcessor):
    """Convert a PDF into a single Markdown file with all images embedded as data URIs.

    Usage:
        PdfToMdInlineProcessor(config_map, persist_fs, pdf_path, md_path=None, use_html_img=False)

    The processor writes the resulting Markdown file to `md_path` (or next to
    the PDF if `md_path` is None).
    """

    def __init__(
        self,
        config_map,  # kept generic to match AProcessor signature
        persist_fs,
        pdf_path: str,
        md_path: Optional[str] = None,
        use_html_img: bool = True,
    ):
        # minimal validation
        self.pdf_path = str(pdf_path)
        self.md_path = md_path
        self.use_html_img = use_html_img
        self.persist_fs = persist_fs
        self.config_map = config_map

    def _convert(self) -> List[str]:
        p = pathlib.Path(self.pdf_path)
        if not p.exists():
            raise FileNotFoundError(f"PDF not found: {self.pdf_path}")

        base = p.stem
        md_file = self.md_path or f"{base}.md"

        doc = fitz.open(self.pdf_path)

        lines: List[str] = [f"# {base}\n"]

        for page_index in range(len(doc)):
            page = doc[page_index]
            page_no = page_index + 1

            try:
                page_md = page.get_text("markdown") or ""
            except Exception:
                page_md = page.get_text() or ""

            lines.append(f"\n\n---\n\n## Page {page_no}\n")
            if page_md.strip():
                lines.append(page_md.strip())

            image_list = page.get_images(full=True)

            if image_list:
                if page_md.strip():
                    lines.append("")
                lines.append("### Images\n")

            for img_i, img in enumerate(image_list, start=1):
                xref = img[0]
                try:
                    info = doc.extract_image(xref)
                except Exception:
                    # Skip if extraction fails
                    continue

                img_bytes = info.get("image", b"")
                ext = info.get("ext", "png")

                if not img_bytes:
                    continue

                data_uri = _to_data_uri(img_bytes, ext)
                alt = f"Page {page_no} image {img_i}"
                if self.use_html_img:
                    # HTML img tag with max-width for readability
                    lines.append(
                        f'<img alt="{alt}" src="{data_uri}" style="max-width:100%">'
                    )
                else:
                    # Pure Markdown image with data URI
                    lines.append(f"![{alt}]({data_uri})")

        return lines, md_file

    def process(self):
        """Run the conversion and persist the output Markdown file."""
        try:
            lines, md_file = self._convert()
            # ensure parent dir exists for md_file
            md_path_obj = pathlib.Path(md_file)
            if md_path_obj.parent and not md_path_obj.parent.exists():
                md_path_obj.parent.mkdir(parents=True, exist_ok=True)

            with open(md_file, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))

            print(f"✅ Saved Markdown with embedded images: {md_file}")
        except Exception as e:
            # keep behavior consistent with other processors using Validator
            try:
                Validator.print_e(e)
            except Exception:
                # fallback to printing
                print(f"Error in PdfToMdInlineProcessor: {e}")
