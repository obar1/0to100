# pylint: disable=W0108
import os


from zero_to_one_hundred.repository.a_persist_fs import APersistFS


class ZTOHPersistFS(APersistFS):
    """ZTOHPersistFS:
    deal with FS
    """

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
