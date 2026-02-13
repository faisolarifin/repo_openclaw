# Hello World REST API - Clean Architecture

REST API sederhana dengan Clean Architecture menggunakan FastAPI.

## 🏗️ Arsitektur

Project ini menggunakan **Clean Architecture** dengan 4 layer utama:

```
hello-api/
├── domain/                 # Layer 1: Entities & Interfaces
│   ├── entities.py        # Business entities
│   └── repositories.py    # Repository interfaces
├── usecase/               # Layer 2: Business Logic
│   └── greeting_usecase.py
├── infrastructure/        # Layer 3: External Concerns
│   └── greeting_repository.py
├── presentation/          # Layer 4: HTTP Handlers
│   └── controllers.py
└── main.py               # Application setup & DI
```

### Layer Dependency Rules

- **Domain** tidak depend ke layer lain (pure business logic)
- **Use Case** hanya depend ke Domain
- **Infrastructure** implement interface dari Domain
- **Presentation** depend ke Use Case

## 🚀 Quick Start

### Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run Server

```bash
python main.py
```

Server akan jalan di `http://localhost:8000`

## 📡 API Endpoints

### 1. Root
```
GET /
```
Informasi API dan list endpoint

### 2. Hello World
```
GET /
```
Response: `{"message": "Hello, World!"}`

### 3. Personalized Greeting
```
GET /greet?name=Faisol&lang=id
```
Response: `{"message": "Halo, Faisol!", "timestamp": "...", "language": "id"}`

**Parameters:**
- `name` (optional, default: "World") - Nama yang akan disapa
- `lang` (optional, default: "en") - Kode bahasa

**Supported languages:**
- `en` - English (Hello)
- `id` - Indonesia (Halo)
- `es` - Spanish (Hola)
- `fr` - French (Bonjour)
- `de` - German (Guten Tag)
- `ja` - Japanese (こんにちは)
- `zh` - Chinese (你好)

### 4. All Greetings
```
GET /greetings
```
List semua greeting yang tersedia

### 5. Health Check
```
GET /health
```
Response: `{"status": "healthy"}`

## 📖 Interactive Documentation

FastAPI menyediakan dokumentasi otomatis:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🧪 Testing

Gunakan curl atau Postman:

```bash
# Hello World
curl http://localhost:8000/

# Custom greeting
curl "http://localhost:8000/greet?name=Faisol&lang=id"

# All greetings
curl http://localhost:8000/greetings

# Health check
curl http://localhost:8000/health
```

## 🏛️ Clean Architecture Benefits

1. **Testability** - Business logic terpisah dari framework
2. **Independence** - Framework, UI, Database bisa diganti
3. **Maintainability** - Separation of concerns yang jelas
4. **Scalability** - Mudah ditambah fitur baru

## 📝 License

MIT
