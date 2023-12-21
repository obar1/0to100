from datetime import datetime


class ProcessFS:
    @staticmethod
    def get_now():
        return datetime.now().strftime("%Y/%m/%d-%H:%M:%S")
