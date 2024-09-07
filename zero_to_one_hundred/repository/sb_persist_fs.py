import json
import logging
from shutil import copyfile

import fitz

from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS

PREFIX_RELATIVE_FOLDER = "./"

# pylint: disable=E1205,W1201


class SBPersistFS(ZTOHPersistFS):
    """SBPersistFS:
    deal with FS
    """

    @classmethod
    def copy_file_to(cls, file_path, path_to):
        logging.info(f"copy_file_to {file_path} {path_to}")
        return copyfile(file_path, path_to)

    @classmethod
    def is_relative_path(cls, path):
        if str(path).startswith(PREFIX_RELATIVE_FOLDER):
            return True
        return False

    @classmethod
    def render_json(cls, txt: str):
        return txt.replace('"', ' " ').replace("\n", " <br/> ")

    @classmethod
    def get_epub_path(cls, download_engine_books_path, isbn, epub_suffix):
        """find the actual path into the path given the isbn
        dirs are supposed to be like
        download_engine_books_path/books title (isbn)
        """
        logging.info(
            f"get_epub_path  {download_engine_books_path} {isbn} {epub_suffix}"
        )
        dirs = cls.list_dirs(download_engine_books_path)
        dir_isbn = [d for d in dirs if "(" + isbn + ")" in d]
        return download_engine_books_path + "/" + dir_isbn[0] + "/" + isbn + epub_suffix

    @classmethod
    def write_fake_epub(cls, path_epub):
        logging.info(f"write_fake_epub {path_epub}")

        HTML = f"""
        <p style="font-family: sans-serif;color: blue">{path_epub}/p>
        """

        MEDIABOX = fitz.paper_rect("letter")  # output page format: Letter
        WHERE = MEDIABOX + (36, 36, -36, -36)  # leave borders of 0.5 inches

        story = fitz.Story(html=HTML)  # create story from HTML
        writer = fitz.DocumentWriter(path_epub)  # create the writer

        more = 1  # will indicate end of input once it is set to 0

        while more:  # loop outputting the story
            device = writer.begin_page(MEDIABOX)  # make new page
            more, _ = story.place(WHERE)  # layout into allowed rectangle
            story.draw(device)  # write on page
            writer.end_page()  # finish page

        writer.close()  # close output file

    @classmethod
    def write_pdf(cls, fn, path_pdf):
        """
        sample from
        https://github.com/pymupdf/PyMuPDF-Utilities/blob/master/examples/convert-document/convert.py
        """
        logging.info(f"write_pdf {fn}")

        doc = fitz.open(fn)

        b = doc.convert_to_pdf()  # convert to pdf
        pdf = fitz.open("pdf", b)  # open as pdf

        toc = doc.get_toc()  # table of contents of input
        pdf.set_toc(toc)  # simply set it for output
        meta = doc.metadata  # read and set metadata
        if not meta["producer"]:
            meta["producer"] = "PyMuPDF v" + fitz.VersionBind

        if not meta["creator"]:
            meta["creator"] = "PyMuPDF PDF converter"
        meta["modDate"] = fitz.get_pdf_now()
        meta["creationDate"] = meta["modDate"]
        pdf.set_metadata(meta)

        # now process the links
        link_cnti = 0
        link_skip = 0
        for pinput in doc:  # iterate through input pages
            links = pinput.get_links()  # get list of links
            link_cnti += len(links)  # count how many
            pout = pdf[pinput.number]  # read corresp. output page
            for l in links:  # iterate though the links
                if l["kind"] == fitz.LINK_NAMED:  # we do not handle named links
                    print("named link page", pinput.number, l)
                    link_skip += 1  # count them
                    continue
                pout.insert_link(l)  # simply output the others

        # save the conversion result
        pdf.save(path_pdf, garbage=4, deflate=True)
        # say how many named links we skipped
        if link_cnti > 0:
            print(
                "Skipped %i named links of a total of %i in input."
                % (link_skip, link_cnti)
            )

    @classmethod
    def write_splitter_pdf(cls, fn, split_pdf_pages):
        """
        split pdf in chunks -easier to manager on ipad with markups
        sample from
        https://github.com/pymupdf/PyMuPDF-Utilities/blob/master/examples/split-document/split.py
        """
        logging.info(f"write_pdf {fn} {split_pdf_pages}")
        fn1 = fn[:-4]
        src = fitz.open(fn)
        last_page = len(src)
        for i in range(1, last_page, split_pdf_pages):
            doc = fitz.open()
            from_page = i
            to_page = i + split_pdf_pages
            doc.insert_pdf(src, from_page=from_page, to_page=to_page)
            doc.save("%s_%i-%i.pdf" % (fn1, from_page, to_page))
            doc.close()

    @classmethod
    def write_json(cls, path_json: str, txt: dict):
        logging.info(f"write_json {path_json} {txt}")
        ZTOHPersistFS.write_file_json(path_json, txt)

    @classmethod
    def read_pages_curr(cls, fn: str) -> int:
        logging.info(f"read_pages_curr {fn}")
        with open(fn, "r", encoding="utf-8") as f:
            json_data = json.loads(f.read())
            logging.info(json_data)
            return int(json_data["page_curr"])

    @classmethod
    def read_pages_tot(cls, fn: str) -> int:
        logging.info(f"read_pages_tot {fn}")
        src = fitz.open(fn)
        logging.info(src)
        return len(src)
