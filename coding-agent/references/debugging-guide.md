# Debugging Guide

## General Debugging Strategy

1. **Reproduce the bug** - Ensure you can consistently trigger the issue
2. **Isolate the problem** - Narrow down where the bug occurs
3. **Form hypothesis** - Guess what might be causing it
4. **Test hypothesis** - Add logging, breakpoints, or tests
5. **Fix and verify** - Implement fix and confirm bug is resolved

## Python Debugging

### Print Debugging
```python
print(f"Debug: variable = {variable}")
print(f"Debug: type = {type(variable)}")
```

### Logging
```python
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug(f"Debug info: {data}")
logger.info("Info message")
logger.warning("Warning message")
logger.error(f"Error: {error}")
```

### PDB (Python Debugger)
```python
import pdb; pdb.set_trace()  # Breakpoint

# Commands:
# n - next line
# s - step into function
# c - continue
# p variable - print variable
# l - list code around current line
# q - quit debugger
```

### FastAPI Debugging
```python
# Enable detailed error messages
app = FastAPI(debug=True)

# Log request/response
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response
```

## Golang Debugging

### Print Debugging
```go
import "fmt"

fmt.Printf("Debug: variable = %v\n", variable)
fmt.Printf("Debug: type = %T\n", variable)
```

### Logging
```go
import "log"

log.Println("Debug info:", data)
log.Printf("Formatted: %v", data)
log.Fatal("Fatal error:", err) // exits program
```

### Delve Debugger
```bash
# Install delve
go install github.com/go-delve/delve/cmd/dlv@latest

# Run with debugger
dlv debug

# Commands:
# b main.go:10 - set breakpoint
# c - continue
# n - next
# s - step into
# p variable - print variable
# q - quit
```

### Gin Debugging
```go
// Enable debug mode
gin.SetMode(gin.DebugMode)

// Logging middleware
router.Use(gin.Logger())
router.Use(gin.Recovery())

// Custom logging
router.Use(func(c *gin.Context) {
    log.Printf("Request: %s %s", c.Request.Method, c.Request.URL)
    c.Next()
    log.Printf("Response status: %d", c.Writer.Status())
})
```

## Common Issues & Solutions

### API Not Responding
1. Check if server is running (`ps aux | grep python` or `ps aux | grep go`)
2. Verify port is not in use (`lsof -i :8000`)
3. Check firewall settings
4. Review server logs for startup errors

### Database Connection Issues
1. Verify connection string/credentials
2. Check if database is running
3. Test connection independently
4. Review connection pool settings

### Race Conditions
**Python:**
```python
from threading import Lock
lock = Lock()

with lock:
    # thread-safe operation
```

**Golang:**
```go
import "sync"
var mu sync.Mutex

mu.Lock()
// critical section
mu.Unlock()
```

### Memory Leaks
**Python:**
- Use `tracemalloc` to track memory usage
- Check for circular references
- Use weak references when appropriate

**Golang:**
- Check for goroutine leaks
- Use pprof for profiling
- Ensure channels are closed

### Slow Performance
1. Profile the code (pprof for Go, cProfile for Python)
2. Check database query performance
3. Look for N+1 queries
4. Review algorithm complexity
5. Check for unnecessary computations in loops

### JSON Parsing Errors
**Python:**
```python
import json
try:
    data = json.loads(json_string)
except json.JSONDecodeError as e:
    print(f"JSON error: {e}")
```

**Golang:**
```go
var data map[string]interface{}
err := json.Unmarshal([]byte(jsonString), &data)
if err != nil {
    log.Printf("JSON error: %v", err)
}
```

## Debugging Tools

### Python
- **pdb** - Built-in debugger
- **ipdb** - Enhanced interactive debugger
- **pytest** - Testing framework with debugging support
- **py-spy** - Sampling profiler
- **memory_profiler** - Memory usage profiler

### Golang
- **delve** - Go debugger
- **pprof** - Profiling tool
- **go test -v** - Verbose test output
- **go vet** - Static analysis
- **golangci-lint** - Comprehensive linter

## Tips

- **Start simple** - Add logging before using debugger
- **Check logs first** - Often errors are already logged
- **Test incrementally** - Test small changes frequently
- **Use version control** - Commit working code frequently
- **Read error messages** - They usually point to the issue
- **Google the error** - Someone likely had the same issue
- **Take breaks** - Fresh eyes often spot bugs faster
