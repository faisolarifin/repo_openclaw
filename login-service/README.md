# Login Service API

Authentication & User Management Service built with FastAPI and Clean Architecture.

## Features

- ✅ User Registration
- ✅ User Login (JWT-based)
- ✅ Token Refresh
- ✅ User Management (CRUD)
- ✅ Password Hashing (bcrypt)
- ✅ Input Validation (Pydantic)
- ✅ Clean Architecture Structure

## Project Structure

```
login-service/
├── app/
│   ├── domain/          # Business entities & exceptions
│   │   ├── entities/    # User entity
│   │   └── exceptions/  # Custom exceptions
│   ├── usecase/         # Business logic
│   ├── infrastructure/  # External concerns (DB, security)
│   │   └── security/    # JWT, password hashing
│   └── presentation/    # HTTP handlers (routes)
├── main.py             # Application entry point
├── requirements.txt    # Dependencies
└── .env.example        # Environment template
```

## Setup

### 1. Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configuration

Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
```

### 3. Run Server

```bash
python main.py
```

Server will run on `http://localhost:8001`

## API Endpoints

### Authentication

**Register User**
```bash
POST /auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "secure_password",
  "full_name": "John Doe"
}
```

**Login**
```bash
POST /auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "secure_password"
}

Response:
{
  "access_token": "eyJ...",
  "refresh_token": "eyJ...",
  "token_type": "bearer"
}
```

**Refresh Token**
```bash
POST /auth/refresh
Authorization: Bearer <refresh_token>

Response:
{
  "access_token": "eyJ...",
  "token_type": "bearer"
}
```

**Logout**
```bash
POST /auth/logout
Authorization: Bearer <access_token>
```

### User Management

**Get Current User**
```bash
GET /users/me
Authorization: Bearer <access_token>
```

**List Users**
```bash
GET /users
Authorization: Bearer <access_token>
```

**Update User**
```bash
PUT /users/{id}
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "full_name": "Jane Doe",
  "email": "jane@example.com"
}
```

**Delete User**
```bash
DELETE /users/{id}
Authorization: Bearer <access_token>
```

### Health Check

```bash
GET /health

Response:
{
  "status": "healthy"
}
```

## Interactive Documentation

After starting the server:
- **Swagger UI**: http://localhost:8001/docs
- **ReDoc**: http://localhost:8001/redoc

## Technology Stack

- **Framework**: FastAPI 0.109.0
- **Authentication**: JWT (python-jose)
- **Password Hashing**: bcrypt (passlib)
- **Validation**: Pydantic
- **Database**: SQLAlchemy 2.0 (SQLite for dev)
- **Server**: Uvicorn

## Security Features

- ✅ Password hashing with bcrypt
- ✅ JWT access tokens (15 min expiry)
- ✅ JWT refresh tokens (7 days expiry)
- ✅ Input validation
- ✅ CORS configuration

## Testing

Run tests:
```bash
pytest tests/ -v
```

## License

MIT
