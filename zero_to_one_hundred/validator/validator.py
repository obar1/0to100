"""TODO."""


def get_abs_path(path: str, curr_path) -> str:
    """get abs path.

    Args:
        curr_path:
    """

    abs_path = path
    if path =='.':
        abs_path = curr_path
    return abs_path


def is_valid_http(txt: str):
    """TODO."""
    assert "https:/" in txt.strip()
    return txt
