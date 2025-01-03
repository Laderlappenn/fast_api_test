import os

from fastapi import APIRouter, Body, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from model.user import User
import service.user as service
from error.exceptions import Missing, Duplicate

ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(prefix="/user")


# --- Новые данные auth
# Эта зависимость создает сообщение в каталоге
# "/user/token" (из формы с именем пользователя и паролем)
# и возвращает токен доступа.
oauth2_dep = OAuth2PasswordBearer(tokenUrl="token")
def unauthed():
    raise HTTPException(
        status_code=401,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )


# К этой конечной точке направляется любой вызов,
# содержащий зависимость oauth2_dep():
@router.post("/token")
async def create_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """Получение имени пользователя и пароля
    из формы OAuth, возврат токена доступа"""
    user = service.auth_user(form_data.username, form_data.password)
    if not user:
        unauthed()
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = service.create_access_token(
        data={"sub": user.username}, expires=expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/token")
def get_access_token(token: str = Depends(oauth2_dep)) -> dict:
    """Возврат текущего токена доступа"""
    return {"token": token}


# CRUD


@router.get("")
def get_all() -> list[User]:
    return service.get_all()


@router.get("/{user_id}", status_code=200, response_model=User)
def get_one(user_id: int) -> User:
    try:
        return service.get_one(user_id)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.post("", status_code=201)
def create(user: User = Body()) -> User:
    try:
        return service.create(user)
    except Duplicate as e:
        raise HTTPException(status_code=409, detail=e.msg)


@router.patch("/{user_id}")
def modify(user_id: int, user: User = Body()) -> User:
    try:
        return service.modify(user_id, user)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.put("/{user_id}")
def replace(user_id: int, user: User = Body()) -> User:
    return service.replace(user_id, user)


@router.delete("/{user_id}")
def delete(user_id: int) -> bool:
    try:
        return service.delete(user_id)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)



