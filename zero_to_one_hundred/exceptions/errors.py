"""Some Exceptions"""


class NotURLFormatError(Exception):
    """NotURLFormatError"""

    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class UnsupportedConfigMapError(Exception):
    """UnsupportedConfigMapError"""

    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class UnsupportedOptionError(Exception):
    """UnsupportedOptionError"""

    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
