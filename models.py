"""
This file contains all custom data models for the project.
"""

from pydantic import BaseModel

from datetime import datetime


class AccessInstance(BaseModel):
    """
    This class is used to log access to a specific room.
    """
    studentId: str
    roomId: str
    blockId: str
    inTime: datetime
    outTime: datetime
