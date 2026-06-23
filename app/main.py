from fastapi import FastAPI
from routers import users
from routers import auth

app = FastAPI(title="My app with PostgreSQL")

app.include_router(users.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "PostgreSQL app running"}
