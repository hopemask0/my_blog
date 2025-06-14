from fastapi import APIRouter, Depends
from typing import List
from app.domain.models.post import PostCreate, PostRead
from app.usecases.post_service import PostService
from app.api.deps import get_post_service

router = APIRouter(prefix="/posts", tags=["posts"])

@router.get("/", response_model=List[PostRead])
def get_all(service: PostService = Depends(get_post_service)):
    return service.get_all_posts()

@router.get("/{post_id}", response_model=PostRead)
def get_by_id(post_id: int, service: PostService = Depends(get_post_service)):
    return service.get_post_by_id(post_id)

@router.get("/search/", response_model=List[PostRead])
def get_by_param(title: str = None, user_id: int = None, service: PostService = Depends(get_post_service)):
    params = {}
    if title is not None:
        params["title"] = title
    if user_id is not None:
        params["user_id"] = user_id
    return service.get_posts_by_param(**params)

@router.post("/", response_model=PostRead)
def create(post: PostCreate, service: PostService = Depends(get_post_service)):
    return service.create_post(post)
