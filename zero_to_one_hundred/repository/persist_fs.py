# pylint: disable=W0108
import os
from datetime import datetime
from shutil import copyfile
from typing import List

import yaml

import sys

import fitz


class PersistFS:
    """PersistFS:
    deal with FS
    mocked in Test"""

    @classmethod
    def list_dirs(cls, path) -> List[str]:
        print(f"list_dirs {path}")
        files = [
            os.path.join(path, name)
            for name in os.listdir(path)
            if os.path.isdir(os.path.join(path, name))
        ]
        files.sort(key=lambda x: os.path.getmtime(x))
        return [f[len(path) + 1 :] for f in files]

    @classmethod
    def get_dir_name(cls, filename):
        return os.path.dirname(os.path.abspath(filename))

    @classmethod
    def load_file(cls, MAP_YAML_PATH):
        with open(MAP_YAML_PATH, mode="r", encoding="UTF-8") as stream:
            return yaml.safe_load(stream)

    @classmethod
    def write_file(cls, filename, txt):
        print(f"write_file {filename}")
        with open(filename, mode="w", encoding="UTF-8") as outfile:
            return outfile.write("".join(txt))

    @classmethod
    def create_file(cls, filename):
        print(f"create_file {filename}")
        return cls.write_file(filename, [])

    @classmethod
    def make_dirs(cls, path):
        print(f"make_dirs {path}")
        return os.makedirs(path, 0o777, True)

    @classmethod
    def read_file(cls, filename) -> List[str]:
        print(f"read_file {filename}")
        with open(filename, mode="r", encoding="UTF-8") as file_:
            lines = file_.readlines()
            return lines

    @classmethod
    def delete_folder(cls, path):
        print(f"delete_folder {path}")
        return os.rmdir(path)

    @classmethod
    def copy_file_to(cls, file_path, path_to):
        print(f"copy_file_to {file_path} {path_to}")
        return copyfile(file_path, path_to)

    @classmethod
    def abs_path(cls, path):
        abs_path = os.path.abspath(path)
        assert abs_path is not None
        print(f"abs_path {abs_path}")
        return abs_path

    @classmethod
    def done_section(cls, path):
        path = cls.abs_path(path)
        print(f"done_section {path}")
        path = path + os.sep + ".done"
        print(f"path {path}")
        os.makedirs(path, 0o777, True)
        with open("{}/.gitkeep".format(path), "a", encoding="utf-8"):
            os.utime("{}/.gitkeep".format(path), None)
        print(f"created {path}")

    @classmethod
    def done_section_status(cls, abs_repo_path, path):
        print(f"done_section_status {path}")
        path = abs_repo_path + os.sep + path + os.sep + ".done"
        print(f"path {path}")
        exists = os.path.exists(path)
        print(f"exists {exists}")
        if exists:
            return True
        return False

    @classmethod
    def write_pdf(cls, fn, path_pdf):
        """
        sample from
        https://github.com/pymupdf/PyMuPDF-Utilities/blob/master/examples/convert-document/convert.py
        """
        print(f"write_pdf {fn}")

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
        print(f"write_pdf {fn} {split_pdf_pages}")
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

 



