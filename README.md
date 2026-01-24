# Title
FastAPI with Async CI/CD

# Installation/ Setup
### Install dependencies 
pip install -r requirements.txt

### Starting the server    
uvicorn app.main:app --reload

# Project description
This project is a simple login system and user management using FastAPI.

Offers:
* User registration and login
* Secured endpoints protected with JWT
* Hashing passwords (Argon2)
* Database (PostgreSQL/ SQLite) with async CRUD
* Endpoints tests using TestClient

# Technologies
* Python 3.10+
* FastAPI
* SQLAlchemy (async)
* JWT for authorization
* Passlib for hashing passwords
* Pytest for tests

# Environment Variables
Create a .env file in the project root with the following variables:
### PostgreSQL
DATABASE_URL=postgresql+asyncpg://user:password@db:5432/dbname

### JWT settings
JWT_SECRET=your_secret_key_here
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60
JWT_ISSUER=myapp

### Optional
DEBUG=True

# Tests
pytest -v

# Docker
The project uses PostgreSQL in a Docker container:   

### Launching the database and application
docker-compose up -d

### Checking FastAPI logs  
docker-compose logs -f app

Default FastAPi port: http://localhost:8000
Default PostgreSQL port: 5432

# CI/CD
The project is prepared for automation in the CI/CD pipeline:
* Automatic tests run on push/pull request
* Optional linting with black / flake8
* Automatic deployment after successful tests



