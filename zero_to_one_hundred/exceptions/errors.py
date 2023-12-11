"""Some Exceptions"""


class NotURLFormatError(Exception):
    """NotURLFormatError"""

    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class UnsupportedConfigMap(Exception):
    """UnsupportedConfigMap"""

    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class UnsupportedOptionError(Exception):
    """UnsupportedOptionError"""

    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
