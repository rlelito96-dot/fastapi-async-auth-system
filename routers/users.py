from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import UserOut, UserUpdate
from app.database import get_db
from app.crud import get_user, update_user, delete_user
from app.auth import get_current_user

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/{user_id}", response_model=UserOut)
async def get_user_endpoint(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = await get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user


@router.put("/{user_id}", response_model=UserOut)
async def update_user_endpoint(
    user_id: int, update_data: UserUpdate, db: AsyncSession = Depends(get_db)
):
    db_user = await get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    data = await update_user(db, db_user, update_data)
    return data


@router.delete("/{user_id}", status_code=204)
async def delete_user_endpoint(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = await get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    await delete_user(db, db_user)
    return
