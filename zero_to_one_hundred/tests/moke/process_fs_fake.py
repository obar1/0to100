from pyfakefs.fake_filesystem_unittest import TestCase
from zero_to_one_hundred.repository.process_fs import ProcessFS


class ProcessFSFake(TestCase, ProcessFS):
    def setUp(self):
        self.setUpPyfakefs()
