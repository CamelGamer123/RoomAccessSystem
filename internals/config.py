"""
This module contains the `Config` class, which is used to store all configuration variables.
"""

from pathlib import Path

from . import createLogger

class Configuration:
    """
    This class stores all configuration variables.
    """

    def __init__(self, configPath: str = Path("Data\\Config.json")):
        """
        This method initializes the `Configuration` class.

        Args:
            configPath (str): The path to the configuration file.
        """

        self.logger = createLogger("Configuration")
