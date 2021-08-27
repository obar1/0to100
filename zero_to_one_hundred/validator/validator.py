"""TODO."""


def is_path(txt: str):
    """TODO."""
    assert "/" in txt.strip()
    return txt


def is_http(txt: str):
    """TODO."""
    assert "https:/" in txt.strip()
    return txt
