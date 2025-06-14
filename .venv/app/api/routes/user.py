from fastapi import APIRouter, Depends
from typing import List
from app.domain.models.user import UserCreate, UserRead
from app.usecases.user_service import UserService
from app.api.deps import get_user_service

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[UserRead])
def get_all(service: UserService = Depends(get_user_service)):
    return service.get_all_users()

@router.get("/{user_id}", response_model=UserRead)
def get_by_id(user_id: int, service: UserService = Depends(get_user_service)):
    return service.get_user_by_id(user_id)

@router.get("/search/", response_model=List[UserRead])
def get_by_param(username: str = None, service: UserService = Depends(get_user_service)):
    params = {}
    if username is not None:
        params["username"] = username
    return service.get_users_by_param(**params)

@router.post("/", response_model=UserRead)
def create(user: UserCreate, service: UserService = Depends(get_user_service)):
    return service.create_user(user)
