class Validator:
    @classmethod
    def is_valid_http(cls, url: str):
        assert "https:/" in url.strip()
