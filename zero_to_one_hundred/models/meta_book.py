import json
import re
import fitz

from zero_to_one_hundred.configs.sb_config_map import SBConfigMap


class MetaBook:
    epub_suffix = ".epub"
    HTTP_OREILLY = "https://learning.oreilly.com/library/cover"
    GENERIC_HTTP_OREILLY = "https://learning.oreilly.com/library/"

    def __init__(self, config_map: SBConfigMap, persist_fs, process_fs, http_url: str):
        self.config_map = config_map
        self.http_url = http_url
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.isbn = self.__get_isbn(http_url)
        self.contents_path = persist_fs.abs_path(f"{self.isbn}")
        self.path_json = f"{self.contents_path}/{self.isbn}.json"
        self.path_epub = f"{self.contents_path}/{self.isbn}.epub"
        self.path_pdf = f"{self.contents_path}/{self.isbn}.pdf"
        self.path_img = f"{self.contents_path}/{self.isbn}.png"

    def __repr__(self):
        return f"MetaBook {self.http_url}, {self.isbn} {self.contents_path}"

    @classmethod
    def build_from_dir(cls, config_map, persist_fs, process_fs, dir_name):
        return MetaBook(
            config_map,
            persist_fs,
            process_fs,
            http_url=cls.GENERIC_HTTP_OREILLY + "/" + dir_name,
        )

    def write_img(self):
        self.process_fs.write_img(self.path_img, f"{self.HTTP_OREILLY}/{self.isbn}/")

    def write_epub(self):
        self.process_fs.write_epub(self.config_map, self.path_epub, self.isbn)
        self.persist_fs.copy_file_to(self.get_epub_path(), self.path_epub)

    def write_json(self):
        """write json
        {
            "isbn": "0596007124",
            "http_url": "https://learning.oreilly.com/library/view/head-first-design/0596007124/"
        }
        """
        txt = []
        txt.append(
            "{"
            + ' "isbn" : "'
            + self.isbn
            + '" '
            + ' ,"url" : "'
            + self.http_url
            + '" '
            + "}"
        )
        self.persist_fs.write_file(
            self.path_json, json.dumps(json.loads("".join(txt)), indent=4)
        )

    @staticmethod
    def is_valid_ebook_path(ebook_folder):
        """check folder is 0123..9 like ISBN"""
        return re.match(r"^[0-9]+", ebook_folder)

    def write(self):
        self.persist_fs.make_dirs(self.contents_path)
        self.write_json()
        self.write_img()
        self.write_epub()
        self.write_pdf()
        self.write_splitter_pdf()

    def read_json(self):
        lines = "{}"
        try:
            lines = self.persist_fs.read_file(self.path_json)
            return json.dumps(json.loads("".join(lines)), indent=4)
        except:
            return lines

    @staticmethod
    def __get_isbn(http_url):
        """get isbn
        it's the last 0123456..9
        """
        http_url = http_url.strip("/")
        return http_url[http_url.rfind("/") + 1 :]

    def get_epub_path(self):
        """find the actual path into the path given the isbn
        dirs are supposed to be like
        download_engine_books_path/books title (isbn)
        """
        download_engine_books_path = self.config_map.get_download_engine_books_path
        isbn = self.isbn
        dirs = self.persist_fs.list_dirs(download_engine_books_path)
        dir_isbn = [dir_ for dir_ in dirs if "(" + isbn + ")" in dir_]
        return (
            download_engine_books_path
            + "/"
            + dir_isbn[0]
            + "/"
            + isbn
            + MetaBook.epub_suffix
        )

    def write_pdf(self):
        """
        sample from
        https://github.com/pymupdf/PyMuPDF-Utilities/blob/master/examples/convert-document/convert.py
        """
        if list(map(int, fitz.VersionBind.split("."))) < [1, 14, 0]:
            raise SystemExit("need PyMuPDF v1.14.0+")
        fn = self.path_epub

        print("Converting '%s' to '%s.pdf'" % (fn, fn))

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
        pdf.save(self.path_pdf, garbage=4, deflate=True)
        # say how many named links we skipped
        if link_cnti > 0:
            print(
                "Skipped %i named links of a total of %i in input."
                % (link_skip, link_cnti)
            )

    def write_splitter_pdf(self):
        """
        split pdf in chunks -easier to manager on ipad with markups
        sample from
        https://github.com/pymupdf/PyMuPDF-Utilities/blob/master/examples/split-document/split.py
        """
        split_pdf_pages = self.config_map.get_split_pdf_pages
        fn = self.path_pdf
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
