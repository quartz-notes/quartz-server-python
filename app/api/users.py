from datetime import timedelta
from typing import Annotated
import jwt
from fastapi import Depends, FastAPI, HTTPException, status,APIRouter
from fastapi.security import  OAuth2PasswordRequestForm

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.core.security import authenticate_user, create_access_token, get_password_hash
from app.models import UserDB
from app.schemas import UserCreate

router = APIRouter()


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[AsyncSession, Depends(get_db)],
) :
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        {"sub": user.username}, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return Token(access_token=access_token, token_type="bearer")


@router.post("/users/")
async def create_user(user: UserCreate, db: Annotated[AsyncSession, Depends(get_db)]):
    hashed_password = get_password_hash(user.password)
    new_user = UserDB(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password,
    )
    db.add(new_user)
    await db.commit()
    return {
        "username": new_user.username,
        "email": new_user.email,
        "full_name": new_user.full_name,
    }
