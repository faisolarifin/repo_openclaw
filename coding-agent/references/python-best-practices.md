# Python Best Practices

## Code Style

- Follow PEP 8 style guide
- Use meaningful variable/function names
- Maximum line length: 88 characters (Black formatter standard)
- Use type hints for function parameters and return values

## Project Structure

```
project/
├── main.py or app.py
├── requirements.txt
├── .env.example
├── README.md
├── models/          # Data models
├── routes/          # API routes
├── services/        # Business logic
├── utils/           # Helper functions
└── tests/           # Unit tests
```

## FastAPI Specific

- Use Pydantic models for request/response validation
- Implement proper error handling with HTTPException
- Add docstrings to all endpoints
- Use dependency injection for shared resources (DB connections, etc.)
- Implement proper logging with Python's logging module
- Use async/await for I/O operations

## Error Handling

```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    item = db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
```

## Environment Variables

- Use python-dotenv for managing environment variables
- Never commit .env files to version control
- Provide .env.example as template

## Testing

- Use pytest for unit testing
- Test coverage should be >80%
- Test edge cases and error scenarios

## Security

- Validate all user input
- Use environment variables for sensitive data
- Implement rate limiting for APIs
- Use CORS middleware properly
- Hash passwords with bcrypt
- Use OAuth2/JWT for authentication

## Performance

- Use async database drivers (asyncpg for PostgreSQL)
- Implement caching where appropriate (Redis)
- Use connection pooling for databases
- Profile slow endpoints with profilers

## Dependencies

- Pin exact versions in requirements.txt for reproducibility
- Regularly update dependencies for security patches
- Use virtual environments (venv)
