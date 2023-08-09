"""
The database access class is contained here.
"""

from sqlite3 import connect, Connection, Cursor
from logging import LoggerAdapter

from . import Configuration, createLogger


class Database:
    """
    This class handles all database access.
    """

    def __init__(self, databasePath: str, config: Configuration):
        """
        This method initializes the database.
        """
        self.logger: LoggerAdapter = createLogger("Database")

        self.logger.info("Initialising Database")

        self.connection: Connection = connect(database=databasePath)
        self.cursor: Cursor = self.connection.cursor()

    def getAccessLogs(self, studentId: str):
        """
        This method returns all access logs of a specific student.

        Args:
            studentId (str): The student ID of the student whose access logs are to be returned.

        Returns:
            list: A list of AccessInstance objects.
        """
        pass
