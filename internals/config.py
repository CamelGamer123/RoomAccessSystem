"""
This module contains the `Config` class, which is used to store all configuration variables.
"""

from pathlib import Path
from typing import Dict
from json import load, dump

from watchdog.events import FileSystemEventHandler

from watchdog.events import DirModifiedEvent, FileModifiedEvent

from . import createLogger


class Configuration:
    """
    This class stores all configuration variables.

    Notes:
        This class should NOT be used to store variables expected to change often.
    """

    def __init__(self, configPath: str = Path("Data\\Config.json")):
        """
        This method initializes the `Configuration` class.

        Args:
            configPath (str): The path to the configuration file.
        """

        self.logger = createLogger("Configuration")

        self.logger.info("Initialising Configuration")
        self.filePath = configPath

        self.logger.info("Configuration class finished initialising")

    """
    ========================================================================================================================
            Get and set methods
    ========================================================================================================================
    """

    def getValue(self, key: str):
        """
        Gets a value from the config.

        Args:
            key (str): The key to get the value for.

        Returns:
            Any: The value for the key.
        """

        # Read the config file
        with open(self.filePath, "r") as f:
            config = load(f)

        # Return the value
        return config[key]

    def writeNewValue(self, key: str, value: Any):
        """
        Writes a new value to the config.

        Args:
            key (str): The key to write the value for.
            value (Any): The value to write.
        """

        # Read the config file
        with open(self.filePath, "r") as f:
            config = load(f)

        # Write the new value
        config[key] = value

        # Write the new config
        with open(self.filePath, "w") as f:
            dump(config, f)
