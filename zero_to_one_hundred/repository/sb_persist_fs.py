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
        dirs = PersistFS.list_dirs(download_engine_books_path)
        dir_isbn = [dir_ for dir_ in dirs if "(" + isbn + ")" in dir_]
        return download_engine_books_path + "/" + dir_isbn[0] + "/" + isbn + epub_suffix
