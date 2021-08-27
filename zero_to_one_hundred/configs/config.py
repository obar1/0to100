"""TODO."""

from validator.validator import is_path


class Config:
    """TODO."""

    def __init__(self, config: dict):
        """Constructor."""
        self._config = config

    def __repr__(self):
        """TODO."""
        return "{} {} {}".format(
            self.get_config_type(), self.get_repo_path(), self.get_repo_sorted()
        )

    def get_config_type(self):
        """Returns config type."""
        return self._config["config"]["type"]

    def get_repo_path(self):
        """Returns path."""
        return is_path(self._config["repo"]["path"])

    def get_repo_sorted(self) -> bool:
        """Returns sorted."""
        return bool(self._config["repo"]["sorted"])
