from pyfakefs.fake_filesystem_unittest import TestCase
from zero_to_one_hundred.repository.sb_process_fs import SBProcessFS


class SBProcessFSFake(TestCase, SBProcessFS):
    pass
