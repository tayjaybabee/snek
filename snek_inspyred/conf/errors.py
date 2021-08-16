"""
A module containing the errors that relate to configuration files.
"""

from pathlib import Path


class AudioConfExistsError(Exception):
    def __init__(self, existing_fp: Path = None, suppress_print: bool = False):
        """

        Raised when there's an instruction to create a new Audio conf file when there's one already present.

        Args:
            existing_fp (str): The path to the existing config file.
                               ( Defaults to NoneType, after initialization the .message/.msg attributes will not
                                 include the path where said AudioConf file resides. )

            suppress_print(bool): By default raising this exception will cause it to print the error message to the
                                  console (if there is one); pass bool(True) as the value here and the exception will
                                  still fill it's .message/.msg attributes, but will not print it to the command-line.
                                  ( Defaults to bool(False) )
        """

        # If there's no value passed to the existing_fp parameter
        if existing_fp is not None:
            fp = existing_fp.absolute()
        else:
            fp = "The filepath in question was not provided."

        # The filepath
        fp = str(fp)

        # Set the message explaining the exception
        self.message = f"The file you're trying to save already exists in the given location: {fp}"
        self.msg = self.message

        # If we should print, we do that.
        if not suppress_print:
            print(self.message)
