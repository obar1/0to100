"""TODO."""

from validator.validator import get_valid_abs_path


class Config:
    """TODO."""

    def __init__(self, config: dict, curr_path):
        """Constructor.

        Args:
            curr_path:
        """
        self.__dict_config = config
        self.__curr_path = curr_path

    def __repr__(self):
        """TODO."""
        return "curr_path:{} dict_config:{}".format(
            self.__curr_path, self.__dict_config
        )

    def get_config_type(self):
        """Returns config type."""
        return self.__dict_config["config"]["type"]

    def get_repo_path(self):
        """Returns path."""
        return get_valid_abs_path(self.__dict_config["repo"]["path"], self.__curr_path)

    def get_repo_sorted(self) -> bool:
        """Returns sorted."""
        return bool(self.__dict_config["repo"]["sorted"])

    def get_curr_path(self):
        """Returns curr_path."""
        return self.__curr_path
