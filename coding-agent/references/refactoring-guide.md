# Refactoring Guide

## When to Refactor

- Code is hard to understand or maintain
- Functions are too long (>50 lines)
- Code duplication exists
- Adding new features is difficult
- Code smells detected
- Before adding new features to messy code

## Code Smells to Watch For

### Long Functions
Split into smaller, focused functions

### Duplicate Code
Extract into reusable functions or classes

### Large Classes
Split into multiple classes with single responsibility

### Long Parameter Lists
Use configuration objects or dependency injection

### Magic Numbers
Replace with named constants

### Deep Nesting
Extract nested logic into separate functions

## Refactoring Techniques

### Extract Function
**Before:**
```python
def process_order(order):
    # validate
    if not order.items:
        raise ValueError("Empty order")
    # calculate total
    total = sum(item.price * item.quantity for item in order.items)
    # apply discount
    if total > 100:
        total *= 0.9
    return total
```

**After:**
```python
def process_order(order):
    validate_order(order)
    total = calculate_total(order)
    total = apply_discount(total)
    return total

def validate_order(order):
    if not order.items:
        raise ValueError("Empty order")

def calculate_total(order):
    return sum(item.price * item.quantity for item in order.items)

def apply_discount(total):
    return total * 0.9 if total > 100 else total
```

### Replace Magic Numbers with Constants
**Before:**
```python
if user.age >= 18:
    allow_access()
```

**After:**
```python
MINIMUM_AGE = 18

if user.age >= MINIMUM_AGE:
    allow_access()
```

### Introduce Parameter Object
**Before:**
```go
func CreateUser(name string, email string, age int, city string, country string) {...}
```

**After:**
```go
type UserInfo struct {
    Name    string
    Email   string
    Age     int
    City    string
    Country string
}

func CreateUser(info UserInfo) {...}
```

### Replace Conditional with Polymorphism
**Before:**
```python
def get_price(product_type, base_price):
    if product_type == "book":
        return base_price * 0.9
    elif product_type == "electronics":
        return base_price * 1.1
    else:
        return base_price
```

**After:**
```python
class Product:
    def get_price(self, base_price):
        return base_price

class Book(Product):
    def get_price(self, base_price):
        return base_price * 0.9

class Electronics(Product):
    def get_price(self, base_price):
        return base_price * 1.1
```

### Simplify Conditional Expressions
**Before:**
```go
if user != nil && user.IsActive && user.Age >= 18 && !user.IsBanned {
    allowAccess()
}
```

**After:**
```go
func canAccess(user *User) bool {
    return user != nil && 
           user.IsActive && 
           user.Age >= 18 && 
           !user.IsBanned
}

if canAccess(user) {
    allowAccess()
}
```

### Extract Variable
**Before:**
```python
return (platform.upper() == "MAC" or platform.upper() == "LINUX") and version >= 10
```

**After:**
```python
is_unix_platform = platform.upper() in ["MAC", "LINUX"]
is_supported_version = version >= 10
return is_unix_platform and is_supported_version
```

## Language-Specific Tips

### Python Refactoring

**Use List Comprehensions**
```python
# Before
squares = []
for i in range(10):
    squares.append(i**2)

# After
squares = [i**2 for i in range(10)]
```

**Use Context Managers**
```python
# Before
f = open('file.txt')
data = f.read()
f.close()

# After
with open('file.txt') as f:
    data = f.read()
```

**Use Dataclasses**
```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    age: int
```

### Golang Refactoring

**Use Struct Embedding**
```go
// Before
type Admin struct {
    Name  string
    Email string
    Role  string
}

// After
type User struct {
    Name  string
    Email string
}

type Admin struct {
    User
    Role string
}
```

**Use Table-Driven Tests**
```go
func TestAdd(t *testing.T) {
    tests := []struct {
        a, b, want int
    }{
        {1, 2, 3},
        {0, 0, 0},
        {-1, 1, 0},
    }
    
    for _, tt := range tests {
        got := Add(tt.a, tt.b)
        if got != tt.want {
            t.Errorf("Add(%d, %d) = %d, want %d", tt.a, tt.b, got, tt.want)
        }
    }
}
```

## Safe Refactoring Process

1. **Have tests** - Write tests if they don't exist
2. **Make small changes** - One refactoring at a time
3. **Run tests** - After each change
4. **Commit frequently** - So you can rollback if needed
5. **Review changes** - Before merging

## Tools

### Python
- **autopep8** - Auto-format code
- **black** - Opinionated code formatter
- **pylint** - Find code smells
- **mypy** - Type checking

### Golang
- **gofmt** - Format code
- **goimports** - Organize imports
- **golangci-lint** - Comprehensive linting
- **go vet** - Find suspicious code

## Remember

- **Don't refactor and add features simultaneously**
- **Keep commits separate** - Refactoring commits vs feature commits
- **Preserve behavior** - Refactoring shouldn't change functionality
- **Measure performance** - If optimizing, benchmark before/after
