"""Concrete implementation of greeting repository"""

from datetime import datetime
from typing import List, Dict
from domain.entities import Greeting
from domain.repositories import GreetingRepository


class InMemoryGreetingRepository(GreetingRepository):
    """In-memory implementation of greeting repository"""
    
    def __init__(self):
        self._greetings: Dict[str, str] = {
            "en": "Hello",
            "id": "Halo",
            "es": "Hola",
            "fr": "Bonjour",
            "de": "Guten Tag",
            "ja": "こんにちは",
            "zh": "你好",
        }
    
    def get_greeting(self, language: str) -> Greeting:
        """Get greeting by language"""
        message = self._greetings.get(language, self._greetings["en"])
        return Greeting(
            message=message,
            timestamp=datetime.now(),
            language=language
        )
    
    def get_all_greetings(self) -> List[Greeting]:
        """Get all available greetings"""
        return [
            Greeting(
                message=msg,
                timestamp=datetime.now(),
                language=lang
            )
            for lang, msg in self._greetings.items()
        ]
