"""Domain entities - Pure business objects"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Greeting:
    """Greeting entity"""
    message: str
    timestamp: datetime
    language: str = "en"
