"""Greeting use cases - Business logic"""

from typing import List
from domain.entities import Greeting
from domain.repositories import GreetingRepository


class GreetingUseCase:
    """Use case for greeting operations"""
    
    def __init__(self, repository: GreetingRepository):
        self.repository = repository
    
    def get_greeting(self, language: str = "en") -> Greeting:
        """Get greeting in specified language"""
        return self.repository.get_greeting(language)
    
    def get_all_greetings(self) -> List[Greeting]:
        """Get all available greetings"""
        return self.repository.get_all_greetings()
    
    def greet(self, name: str = "World", language: str = "en") -> str:
        """Generate personalized greeting"""
        greeting = self.repository.get_greeting(language)
        return f"{greeting.message}, {name}!"
