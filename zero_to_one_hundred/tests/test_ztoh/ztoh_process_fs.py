from zero_to_one_hundred.repository.ztoh_process_fs import ZTOHProcessFS as zfs


class ZTOHProcessFS(zfs):
    @staticmethod
    def get_now():
        return "2099/01/01 - 00:00:00"
