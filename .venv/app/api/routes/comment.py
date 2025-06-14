from fastapi import APIRouter, Depends
from typing import List
from app.domain.models.comment import CommentCreate, CommentRead
from app.usecases.comment_service import CommentService
from app.api.deps import get_comment_service

router = APIRouter(prefix="/comments", tags=["comments"])

@router.get("/", response_model=List[CommentRead])
def get_all(service: CommentService = Depends(get_comment_service)):
    return service.get_all_comments()

@router.get("/{comment_id}", response_model=CommentRead)
def get_by_id(comment_id: int, service: CommentService = Depends(get_comment_service)):
    return service.get_comment_by_id(comment_id)

@router.get("/search/", response_model=List[CommentRead])
def get_by_param(post_id: int = None, user_id: int = None, service: CommentService = Depends(get_comment_service)):
    params = {}
    if post_id is not None:
        params["post_id"] = post_id
    if user_id is not None:
        params["user_id"] = user_id
    return service.get_comments_by_param(**params)

@router.post("/", response_model=CommentRead)
def create(comment: CommentCreate, service: CommentService = Depends(get_comment_service)):
    return service.create_comment(comment)
