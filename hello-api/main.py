"""Main application - Dependency injection and setup"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Import layers
from infrastructure.greeting_repository import InMemoryGreetingRepository
from usecase.greeting_usecase import GreetingUseCase
from presentation.controllers import GreetController

# Initialize FastAPI app
app = FastAPI(
    title="Hello World API",
    description="Clean Architecture REST API Demo",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency Injection - Wire up layers
def setup_dependencies():
    """Setup dependency injection"""
    # Infrastructure layer
    greeting_repo = InMemoryGreetingRepository()
    
    # Use case layer
    greeting_usecase = GreetingUseCase(repository=greeting_repo)
    
    # Presentation layer
    greet_controller = GreetController(usecase=greeting_usecase)
    
    return greet_controller

# Setup and register routes
controller = setup_dependencies()
app.include_router(controller.router, tags=["Greetings"])

# Root endpoint
@app.get("/")
async def root():
    """API root"""
    return {
        "name": "Hello World API",
        "version": "1.0.0",
        "architecture": "Clean Architecture",
        "endpoints": {
            "hello": "/",
            "greet": "/greet?name=YourName&lang=en",
            "all_greetings": "/greetings",
            "health": "/health"
        }
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
