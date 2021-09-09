"""TODO:
"""
# pylint: disable=R0903,E0401,W0703,W1201

class Validator:

    def __init__(self,relative_path_starts_with,repo_path, yaml_abs_path):
        self.relative_path_starts_with=relative_path_starts_with
        self.repo_path=repo_path
        self.yaml_abs_path=yaml_abs_path

    @property
    def build_full_path(self ) -> str:
        """get abs path."""
        return (self.yaml_abs_path+'/'+self.repo_path[2:]) if self.repo_path.startswith(self.relative_path_starts_with) else self.repo_path

    @classmethod
    def is_valid_http(cls, txt: str):
        """is_valid_http
        basic validation """
        assert "https:/" in txt.strip()
        return txt
