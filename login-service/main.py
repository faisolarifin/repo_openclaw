from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
    title="Login Service API",
    description="Authentication & User Management Service with Clean Architecture",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root
@app.get("/")
async def root():
    return {
        "name": "Login Service API",
        "version": "1.0.0",
        "endpoints": {
            "register": "POST /auth/register",
            "login": "POST /auth/login",
            "logout": "POST /auth/logout",
            "refresh": "POST /auth/refresh",
            "me": "GET /users/me",
            "users": "GET /users",
            "health": "GET /health"
        }
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
