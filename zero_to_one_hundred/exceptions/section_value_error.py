"""SectionValueError:
"""
# pylint: disable=R0903,E0401,W0703
class SectionValueError(Exception):
    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

        # Now for your custom code...
        self.errors = errors
