# Golang Best Practices

## Code Style

- Follow official Go style guide (gofmt, golint)
- Use meaningful package, variable, and function names
- Export only what's necessary (capitalize for public, lowercase for private)
- Write idiomatic Go code

## Project Structure

```
project/
├── main.go
├── go.mod
├── go.sum
├── .env.example
├── README.md
├── cmd/             # Application entry points
├── internal/        # Private application code
│   ├── handlers/    # HTTP handlers
│   ├── models/      # Data models
│   └── services/    # Business logic
├── pkg/             # Public libraries
└── tests/           # Integration tests
```

## Gin Framework Specific

- Use router groups for related endpoints
- Implement middleware for cross-cutting concerns (logging, auth)
- Use binding for request validation
- Return proper HTTP status codes
- Handle errors gracefully

## Error Handling

```go
if err != nil {
    c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
    return
}
```

Always check errors and handle them appropriately. Never ignore errors.

## Concurrency

- Use goroutines for concurrent operations
- Use channels for communication between goroutines
- Always use mutex for shared data access
- Avoid goroutine leaks (always ensure goroutines can exit)

```go
var mu sync.Mutex
mu.Lock()
// critical section
mu.Unlock()
```

## Environment Variables

- Use godotenv or viper for configuration
- Never hardcode sensitive data
- Provide .env.example template

## Testing

- Write unit tests with the testing package
- Use table-driven tests for multiple test cases
- Aim for >80% code coverage
- Use mockery or gomock for mocking dependencies

```go
func TestGetItem(t *testing.T) {
    // test implementation
}
```

## Security

- Validate all user input
- Use environment variables for secrets
- Implement rate limiting
- Use CORS middleware properly
- Hash passwords with bcrypt
- Use JWT for authentication

## Performance

- Use connection pooling for databases
- Implement caching where appropriate
- Profile with pprof for bottlenecks
- Use buffered channels for performance
- Avoid unnecessary allocations

## Dependencies

- Use Go modules (go.mod) for dependency management
- Run `go mod tidy` regularly
- Pin versions for reproducibility
- Update dependencies for security patches

## Common Patterns

### Middleware
```go
func Logger() gin.HandlerFunc {
    return func(c *gin.Context) {
        // before request
        c.Next()
        // after request
    }
}
```

### Graceful Shutdown
```go
srv := &http.Server{Addr: ":8000", Handler: r}
go srv.ListenAndServe()

quit := make(chan os.Signal, 1)
signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
<-quit

ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel()
srv.Shutdown(ctx)
```
