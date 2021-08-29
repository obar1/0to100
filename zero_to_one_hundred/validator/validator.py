"""TODO."""


def get_valid_abs_path(txt: str, curr_path) -> str:
    """get abs path.

    Args:
        curr_path:
    """
    assert "/" in txt.strip()

    abs_path = txt
    if txt.startswith("./"):
        abs_path = curr_path + "/" + txt[2:]
    return abs_path.replace("//", "/")


def is_valid_http(txt: str):
    """TODO."""
    assert "https:/" in txt.strip()
    return txt
