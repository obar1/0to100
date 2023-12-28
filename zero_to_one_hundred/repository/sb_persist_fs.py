import json
import fitz

from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.repository.persist_fs import PersistFS

PREFIX_RELATIVE_FOLDER = "./"


class SBPersistFS(PersistFS):
    """SBPersistFS:
    deal with FS
    mocked in Test"""

    @classmethod
    def is_relative_path(cls, path):
        if str(path).startswith(PREFIX_RELATIVE_FOLDER):
            return True
        return False

    @classmethod
    def render_json(cls, txt: str):
        return txt.replace('"', ' " ').replace("\n", " <br/> ")

    @classmethod
    def render_path(cls, txt: str):
        return txt.replace(" ", "%20")

    @classmethod
    def get_epub_path(cls, download_engine_books_path, isbn, epub_suffix):
        """find the actual path into the path given the isbn
        dirs are supposed to be like
        download_engine_books_path/books title (isbn)
        """
        print(f"get_epub_path  {download_engine_books_path} {isbn} {epub_suffix}")
        dirs = PersistFS.list_dirs(download_engine_books_path)
        dir_isbn = [dir_ for dir_ in dirs if "(" + isbn + ")" in dir_]
        return download_engine_books_path + "/" + dir_isbn[0] + "/" + isbn + epub_suffix

    @classmethod
    def write_fake_epub(cls, path_epub):
        print(f"write_fake_epub  {path_epub}")
 
        HTML = """
        <p style="font-family: sans-serif;color: blue">Hello World!</p>
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
    def write_json(cls, path_json: str, txt:str):
        print(f"write_json {path_json} {txt}")
        PersistFS.write_file(path_json, json.dumps(json.loads("".join(txt)), indent=4))