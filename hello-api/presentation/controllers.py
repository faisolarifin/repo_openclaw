"""HTTP controllers/handlers"""

from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from usecase.greeting_usecase import GreetingUseCase


class GreetingResponse(BaseModel):
    """Response model for greeting"""
    message: str
    timestamp: datetime
    language: str


class GreetController:
    """Controller for greeting endpoints"""
    
    def __init__(self, usecase: GreetingUseCase):
        self.usecase = usecase
        self.router = APIRouter()
        self._setup_routes()
    
    def _setup_routes(self):
        """Setup all routes"""
        
        @self.router.get("/", response_model=dict)
        async def hello_world():
            """Simple hello world endpoint"""
            return {"message": "Hello, World!"}
        
        @self.router.get("/greet", response_model=dict)
        async def greet(
            name: str = Query(default="World", description="Name to greet"),
            lang: str = Query(default="en", description="Language code")
        ):
            """Personalized greeting endpoint"""
            message = self.usecase.greet(name=name, language=lang)
            return {
                "message": message,
                "timestamp": datetime.now(),
                "language": lang
            }
        
        @self.router.get("/greetings", response_model=List[GreetingResponse])
        async def get_all_greetings():
            """Get all available greetings"""
            greetings = self.usecase.get_all_greetings()
            return [
                GreetingResponse(
                    message=g.message,
                    timestamp=g.timestamp,
                    language=g.language
                )
                for g in greetings
            ]
        
        @self.router.get("/health")
        async def health_check():
            """Health check endpoint"""
            return {"status": "healthy"}
