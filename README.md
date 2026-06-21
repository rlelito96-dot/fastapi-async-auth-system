# 🔐 FastAPI Async Authentication System

A lightweight backend API built with FastAPI for user authentication and management.  
It provides JWT-based security, async PostgreSQL access, and secure password hashing.

---

## 🚀 Quick Start

```bash
cp .env.example .env
docker compose up -d
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 📦 Full Setup

### 1. Clone repository

```bash
git clone https://github.com/your-username/fastapi-async-auth-system.git
cd faas
```

### 2. Create environment file

```bash
cp .env.example .env
```

### 3. Start database (Docker)

```bash
docker compose up -d
```

### 4. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / WSL
venv/Scripts/activate   # Windows
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Starting the server    

```bash
uvicorn app.main:app --reload
```

---

# 📌 Project description
This project is a simple login system and user management using FastAPI.

Offers:
* User registration and login
* Secured endpoints protected with JWT
* Hashing passwords (Argon2)
* Database (PostgreSQL/ SQLite) with async CRUD
* Endpoints tests using TestClient

---

# 🧰 Technologies
* Python 3.10+
* FastAPI
* SQLAlchemy (async)
* JWT for authorization
* Passlib for hashing passwords
* Pytest for tests

---

# 🧪 Tests

```bash
pytest -vvv
```

---

# 📖 API Documentation

- *API*: http://localhost:8000
- *Swagger docs*: http://localhost:8000/docs
- *Redoc*: http://localhost:8000/redoc

---

# 🔄 CI/CD
The project is prepared for automation in the CI/CD pipeline:
* Automatic tests run on push/pull request
* Optional linting with black / flake8
* Automatic deployment after successful tests



