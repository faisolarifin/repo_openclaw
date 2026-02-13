"""Repository interfaces - Define contracts"""

from abc import ABC, abstractmethod
from typing import List
from domain.entities import Greeting


class GreetingRepository(ABC):
    """Interface for greeting repository"""
    
    @abstractmethod
    def get_greeting(self, language: str) -> Greeting:
        """Get greeting by language"""
        pass
    
    @abstractmethod
    def get_all_greetings(self) -> List[Greeting]:
        """Get all available greetings"""
        pass
