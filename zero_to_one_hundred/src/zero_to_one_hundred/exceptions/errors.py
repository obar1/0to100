class NotURLFormatError(Exception):
    def __init__(self, message):
        super().__init__(message)


class UnsupportedConfigMapError(Exception):
    def __init__(self, message):
        super().__init__(message)


class UnsupportedOptionError(Exception):
    def __init__(self, message):
        super().__init__(message)


class SomeError(Exception):
    def __init__(self, message):
        super().__init__(message)
