import jwt, os
from fastapi import Depends, Header, HTTPException, status
from passlib.context import CryptContext
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
JWT_EXPIRE_MINUTES = os.getenv("JWT_EXPIRE_MINUTES")
JWT_ISSUER = os.getenv("JWT_ISSUER")

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed) -> bool:
    return pwd_context.verify(password, hashed)

def issue_jwt(user_id: int, role: str) -> str:
    header = {
        "alg": JWT_ALGORITHM,
        "typ": "JWT"
    }

    payload = {
        "user_id": user_id,
        "role": role,
        "iat": int(datetime.now(timezone.utc).timestamp()),
        "exp": int((datetime.now(timezone.utc) + timedelta(minutes=JWT_EXPIRE_MINUTES)).timestamp()),
        "iss": JWT_ISSUER
    }

    token = jwt.encode(JWT_SECRET, payload, algorithms=JWT_ALGORITHM, headers=header)
    return token

def verify_jwt(token: str) -> dict:
    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        if decoded.get("iss") != JWT_ISSUER:
            raise HTTPException(status_code=401, detail="Invalid token")

        return decoded

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


def get_current_user(authorization: str = Header(...)) -> dict:
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=401, detail="Invalid authorization")
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid authorization")

    return verify_jwt(token)


