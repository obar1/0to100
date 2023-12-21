from pyfakefs.fake_filesystem_unittest import TestCase
from zero_to_one_hundred.repository.sb_persist_fs import SBPersistFS


class SBPersistFSFake(TestCase, SBPersistFS):
    @classmethod
    def setUpClass(cls):
        cls.setUpClassPyfakefs()
