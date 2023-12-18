from pyfakefs.fake_filesystem_unittest import TestCase
from zero_to_one_hundred.repository.persist_fs import PersistFS


class PersistFSFake(TestCase, PersistFS):
    def setUp(self):
        self.setUpPyfakefs()
