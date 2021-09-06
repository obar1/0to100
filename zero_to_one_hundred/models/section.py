"""TODO."""


# pylint: disable=R0903,E0401,W0703,W0238
class Section:
    """TODO."""

    @classmethod
    def from_str(cls, http_url: str):
        return Section(http_url)

    def __init__(self, http_url: str):
        """
        Init
        Args:
            http_url: https://cloud.google.com/docs
        """
        self.__http_url = http_url

    def __str__(self):
        return "Section from {}".format(self.__http_url)

    def get_valid_path(self, repo_path) -> str:
        """
        Convert
        Returns:
            str: https:§§cloud.google.com§docs
        """
        return repo_path + "/" + self.http_url_as_section()

    def http_url_as_section(self):
        return self.__http_url.replace("/", "§")

    def get_section(self):
        return self.http_url_as_section()

    def get_http(self):
        return self.__http_url
