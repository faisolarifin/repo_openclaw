# Code Review Checklist

Use this checklist when reviewing code to ensure quality, security, and maintainability.

## Functionality

- [ ] Code implements the intended functionality correctly
- [ ] Edge cases are handled properly
- [ ] Error handling is comprehensive
- [ ] No obvious bugs or logic errors

## Code Quality

- [ ] Code is readable and self-documenting
- [ ] Variable/function names are clear and meaningful
- [ ] Functions are small and focused (single responsibility)
- [ ] No code duplication (DRY principle)
- [ ] Complex logic has comments explaining why
- [ ] No commented-out code (use version control instead)

## Style & Conventions

- [ ] Follows language-specific style guide (PEP 8 for Python, gofmt for Go)
- [ ] Consistent naming conventions
- [ ] Proper indentation and formatting
- [ ] Imports are organized and necessary

## Testing

- [ ] Unit tests are included
- [ ] Tests cover happy path and edge cases
- [ ] Tests are meaningful and maintainable
- [ ] All tests pass

## Security

- [ ] User input is validated and sanitized
- [ ] No sensitive data in code or logs
- [ ] Authentication/authorization is properly implemented
- [ ] SQL injection prevention (use parameterized queries)
- [ ] XSS prevention (escape user input)
- [ ] Secrets are in environment variables, not hardcoded

## Performance

- [ ] No obvious performance issues
- [ ] Database queries are optimized
- [ ] No N+1 query problems
- [ ] Appropriate use of caching
- [ ] No unnecessary loops or computations

## Documentation

- [ ] README is updated if needed
- [ ] API documentation is updated
- [ ] Complex functions have docstrings
- [ ] Environment variables are documented

## Dependencies

- [ ] No unnecessary dependencies added
- [ ] Dependencies are pinned to specific versions
- [ ] Security vulnerabilities checked

## Database/Data

- [ ] Database migrations are included if schema changed
- [ ] Data validation is in place
- [ ] Transactions are used appropriately
- [ ] No race conditions with concurrent access

## API Design (for REST APIs)

- [ ] Proper HTTP methods used (GET, POST, PUT, DELETE)
- [ ] Appropriate status codes returned
- [ ] Request/response models are well-defined
- [ ] Versioning strategy if applicable
- [ ] Rate limiting considered

## Specific Language Checks

### Python
- [ ] Type hints are used
- [ ] Virtual environment setup documented
- [ ] requirements.txt is updated
- [ ] No blocking calls in async functions

### Golang
- [ ] Errors are checked and handled
- [ ] No goroutine leaks
- [ ] Mutex used for shared data
- [ ] go.mod and go.sum are updated
- [ ] Context used for cancellation/timeouts

## Final Checks

- [ ] Build succeeds without errors
- [ ] No linting errors
- [ ] Code runs successfully in development
- [ ] Breaking changes are documented
- [ ] Rollback plan exists for risky changes
