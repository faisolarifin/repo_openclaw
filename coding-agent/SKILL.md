---
name: coding-agent
description: Comprehensive coding assistant for Python and Golang development. Use when building projects from scratch, reviewing code, debugging issues, refactoring code, or creating REST APIs. Supports FastAPI (Python) and Gin (Golang) frameworks with boilerplate templates, best practices, and debugging guides.
---

# Coding Agent

Professional coding assistance for Python and Golang development, covering the full software development lifecycle from project creation to debugging and refactoring.

## Core Capabilities

1. **Project Creation** - Bootstrap new projects with production-ready templates
2. **Code Review** - Systematic code quality and security review
3. **Debugging** - Systematic issue identification and resolution
4. **Refactoring** - Improve code quality and maintainability
5. **REST API Development** - Build APIs with FastAPI or Gin framework

## Quick Start

### Creating a New Project

**Python FastAPI:**
Copy the template from `assets/templates/python-fastapi/` to your project directory. The template includes:
- `main.py` - CRUD REST API with health check endpoint
- `requirements.txt` - FastAPI, Uvicorn, Pydantic dependencies
- `.env.example` - Environment variable template

**Golang Gin:**
Copy the template from `assets/templates/golang-gin/` to your project directory. The template includes:
- `main.go` - CRUD REST API with health check endpoint
- `go.mod` - Module definition with Gin dependency
- `.env.example` - Environment variable template

Both templates provide:
- Health check endpoint (`/health`)
- Full CRUD operations (`GET`, `POST`, `PUT`, `DELETE`)
- Request validation
- Error handling
- Concurrent-safe implementation

### Running Projects

**Python:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

**Golang:**
```bash
go mod download
go run main.go
```

Both run on `http://localhost:8000` by default.

## Development Workflows

### 1. Code Review

When reviewing code, consult `references/code-review-checklist.md` for comprehensive checklist covering:
- Functionality and correctness
- Code quality and readability
- Security vulnerabilities
- Performance considerations
- Testing coverage
- Language-specific checks (Python/Golang)

Present findings as:
1. Critical issues (security, bugs)
2. Important improvements (performance, maintainability)
3. Nice-to-have suggestions (style, conventions)

### 2. Debugging

Follow systematic debugging process from `references/debugging-guide.md`:

1. **Reproduce** - Confirm the bug consistently occurs
2. **Isolate** - Narrow down the problem location
3. **Hypothesize** - Form theory about the cause
4. **Test** - Add logging, use debuggers, write tests
5. **Fix** - Implement solution and verify

**Python debugging tools:**
- Print debugging with f-strings
- Logging module for structured logs
- pdb for interactive debugging
- FastAPI debug mode for detailed errors

**Golang debugging tools:**
- fmt.Printf for quick debugging
- log package for structured logging
- Delve debugger for step-through debugging
- Gin debug mode and middleware

Common issues covered: API not responding, database connections, race conditions, memory leaks, performance issues.

### 3. Refactoring

Apply refactoring patterns from `references/refactoring-guide.md`:

**When to refactor:**
- Functions exceed 50 lines
- Code duplication exists
- Hard to add new features
- Code smells detected

**Safe refactoring process:**
1. Ensure tests exist
2. Make small, incremental changes
3. Run tests after each change
4. Commit frequently
5. Review before merging

**Common techniques:**
- Extract function (split long functions)
- Replace magic numbers with constants
- Introduce parameter objects
- Simplify conditionals
- Remove code duplication

### 4. Best Practices

**For Python projects:**
Consult `references/python-best-practices.md` for:
- PEP 8 style compliance
- Project structure conventions
- FastAPI-specific patterns (async/await, dependency injection)
- Security practices (input validation, authentication)
- Performance optimization (async drivers, caching)

**For Golang projects:**
Consult `references/golang-best-practices.md` for:
- Idiomatic Go code style
- Project structure (cmd/, internal/, pkg/)
- Gin framework patterns (middleware, router groups)
- Concurrency safety (goroutines, mutexes, channels)
- Error handling best practices

## REST API Development

### Endpoints Pattern

Both templates follow RESTful conventions:

```
GET    /health          - Health check
GET    /items           - List all items
GET    /items/:id       - Get specific item
POST   /items           - Create new item
PUT    /items/:id       - Update item
DELETE /items/:id       - Delete item
```

### Extending Templates

To add new resources:

**Python:**
```python
class NewResource(BaseModel):
    field1: str
    field2: int

@app.post("/resources", response_model=NewResource)
async def create_resource(resource: NewResource):
    # implementation
    return resource
```

**Golang:**
```go
type NewResource struct {
    Field1 string `json:"field1" binding:"required"`
    Field2 int    `json:"field2" binding:"required"`
}

router.POST("/resources", func(c *gin.Context) {
    var resource NewResource
    if err := c.ShouldBindJSON(&resource); err != nil {
        c.JSON(400, gin.H{"error": err.Error()})
        return
    }
    c.JSON(201, resource)
})
```

## Resources

### Templates (`assets/templates/`)
- **python-fastapi/** - FastAPI REST API boilerplate
- **golang-gin/** - Gin framework REST API boilerplate

### References (`references/`)
- **python-best-practices.md** - Python/FastAPI development standards
- **golang-best-practices.md** - Golang/Gin development standards
- **code-review-checklist.md** - Comprehensive review checklist
- **debugging-guide.md** - Systematic debugging strategies
- **refactoring-guide.md** - Code improvement techniques

Load reference files only when needed for specific tasks.
