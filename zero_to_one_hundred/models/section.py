"""TODO."""


# pylint: disable=R0903,E0401,W0703,W0238
class Section:
    """TODO."""

    @classmethod
    def from_str(cls, txt: str):
        http_url = txt
        return Section(http_url)

    def __init__(self, http_url: str):
        """
        Init
        Args:
            http_url: https://cloud.google.com/docs
        """
        self.__http_url = http_url

    def __repr__(self):
        return "http_url={}".format(self.__http_url)

    def get_valid_path(self, repo_path) -> str:
        """
        Convert
        Returns:
            str: https:§§cloud.google.com§docs
        """
        return repo_path + "/" + self.__http_url.replace("/", "§")
