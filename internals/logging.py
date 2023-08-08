"""
This module contains all logging related code for the project and wraps the logging module for extra functionality.
"""

from logging import FileHandler, StreamHandler, getLogger, Formatter, DEBUG, INFO, WARNING, ERROR, CRITICAL, \
    LoggerAdapter
from os import getcwd, path, mkdir
from datetime import datetime
from sys import stdout
from pathlib import Path


def getColourCode(
        baseColour: str,
        bold: bool = False,
        underline: bool = False,
) -> str:
    """
    Gets the ANSI escape code for the given colour.

    Args:
        baseColour (str): The base colour to get the ANSI escape code for.
        bold (bool): Whether the text should be bold.
        underline (bool): Whether the text should be underlined.

    Returns:
        str: The ANSI escape code for the given colour.

    Raises:
        ValueError: If the given colour is not a valid colour.

    Reference:
        https://gist.github.com/JBlond/2fea43a3049b38287e5e9cefc87b2124
    """
    if baseColour.endswith("_H"):  # Specifies that the colour is of a high intensity. (Defined as 90-97)
        baseColour = baseColour[:-2]
        highIntensity = True
    else:
        highIntensity = False

    match baseColour.upper():
        case "BLACK":
            colourCode = 30
        case "RED":
            colourCode = 31
        case "GREEN":
            colourCode = 32
        case "YELLOW":
            colourCode = 33
        case "BLUE":
            colourCode = 34
        case "PURPLE":
            colourCode = 35
        case "CYAN":
            colourCode = 36
        case "WHITE":
            colourCode = 37
        case _:
            raise ValueError(f"{baseColour} is not a valid colour.")

    if highIntensity:
        colourCode += 60

    if bold:
        formatter = "1;"
    elif underline:
        formatter = "4;"
    elif bold and underline:
        formatter = "1;4;"
    else:
        formatter = ""
    # Assemble the ANSI escape code
    return f"\033[{formatter}{colourCode}m"


class ColourCodedFormatter(Formatter):
    """
    A formatter that adds colour coding to the log messages.
    """

    def __init__(self, fmt=None, datefmt=None, style='%',
                 colourCoding: dict = None
                 ):
        super().__init__(fmt, datefmt, style)

        if colourCoding is None:
            colourCoding = {
                "DEBUG": getColourCode("CYAN"),
                "INFO": getColourCode("GREEN"),
                "WARNING": getColourCode("YELLOW"),
                "ERROR": getColourCode("RED"),
                "CRITICAL": getColourCode("RED_H"),
            }
        self.colourCoding = colourCoding

    def format(self, record):
        """
        Formats the log message.

        Args:
            record (LogRecord): The log record to format.

        Returns:
            str: The formatted log message.
        """
        try:
            record.levelname = f"{self.colourCoding[record.levelname]}{record.levelname}\033[0m"
        except KeyError:  # Handles the case where the level name is not in the colour coding dictionary
            pass
        return super().format(record)


def createLogger(
        name: str,
        loggingDirectory: str = None,
        logFileName: str = None,
        level: str = "DEBUG",
        formatString: str = "[%(asctime)s] [%(loggerName)s] [%(levelname)s] %(message)s",
        handlers: list = None,
        doColour: bool = True,
        colourCoding: dict = None
) -> LoggerAdapter:
    """
    Creates a logger with the specified name, logging path, level, and formatter.

    Args:
        name (str): The name of the logger.
        loggingDirectory (str): The path to the logging directory.
        logFileName (str): The name of the log file.
        level (str): The level of the logger.
        formatString (str): The format string for the logger.
        handlers (list): Additional handlers for the logger.
        doColour (bool): Whether to use colour coding in the logger for logging outputs.
        colourCoding (dict): The colour coding for the logger. Defaults to the default colour coding defined in the
            function.

    Returns:
        logger (Logger): The logger object.

    """
    if loggingDirectory is None:
        loggingDirectory = name

    if logFileName is None:
        logFileName = ""

    if not path.exists(Path(f'{getcwd()}\\Logs')):
        mkdir(Path(f'{getcwd()}\\Logs'))

    # Check if the logging directory exists, if not, create it
    if not path.exists(Path(f'{getcwd()}\\Logs\\{loggingDirectory}')):
        mkdir(Path(f'{getcwd()}\\Logs\\{loggingDirectory}'))

    match level.lower():
        case "debug":
            level = DEBUG
        case "info":
            level = INFO
        case "warning":
            level = WARNING
        case "error":
            level = ERROR
        case "critical":
            level = CRITICAL
        case _:
            raise ValueError('Invalid level specified')

    logger = getLogger(name)  # Sets the logger's name
    logger.setLevel(level)  # Sets the logger's level

    if logger.hasHandlers():  # This checks if the logger has already been created and if it has, it replaces the
        # handlers with the new ones
        logger.handlers.clear()

    if handlers is None:
        handlers = [
            FileHandler(
                Path(
                    f'{getcwd()}\\Logs\\{loggingDirectory}\\{logFileName}{datetime.now().strftime("%d.%m.%Y")}.log'
                ),
                encoding='utf-8'
            ),  # Creates the file handler for the logger
            StreamHandler(stdout)  # Creates the stream handler for the logger
        ]

    colourFormatter = ColourCodedFormatter(formatString)
    formatter = Formatter(formatString)

    for handler in handlers:
        if not doColour or isinstance(handler, FileHandler):
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            pass

        else:
            handler.setFormatter(colourFormatter)
            logger.addHandler(handler)

    # A logger adapter is used here to allow for the logger name to be included in the log messages. This is useful
    # when multiple loggers are used in the same project.
    logger = LoggerAdapter(logger, {'loggerName': name})
    return logger
