from fastapi import Depends
from sqlalchemy.orm import Session
from app.infrastructure.db.session import SessionLocal
from app.infrastructure.repositories.post_repo_impl import PostRepositoryImpl
from app.infrastructure.repositories.comment_repo_impl import CommentRepositoryImpl
from app.infrastructure.repositories.user_repo_impl import UserRepositoryImpl
from app.usecases.post_service import PostService
from app.usecases.comment_service import CommentService
from app.usecases.user_service import UserService

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_post_service(db: Session = Depends(get_db)):
    repo = PostRepositoryImpl(db)
    return PostService(repo)

def get_comment_service(db: Session = Depends(get_db)):
    repo = CommentRepositoryImpl(db)
    return CommentService(repo)

def get_user_service(db: Session = Depends(get_db)):
    repo = UserRepositoryImpl(db)
    return UserService(repo)
