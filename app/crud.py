from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import User
from app.auth import hash_password

async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).filter(User.id == user_id))
    return result.scalars().first()

async def get_user_by_name(db: AsyncSession, name: str):
    result = await db.execute(select(User).filter(User.name == name))
    return result.scalars().first()

async def create_user(db: AsyncSession, user_data):
    db_user = User(
        name=user_data.name,
        website=user_data.website,
        age=user_data.age,
        role=user_data.role,
        password_hash=hash_password(user_data.password)
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def update_user(db: AsyncSession, db_user, update_data):
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(db_user, key, value)

    await db.commit()
    await db.refresh(db_user)
    return db_user

async def delete_user(db: AsyncSession, db_user):
    await db.delete(db_user)
    await db.commit()