from app.infrastructure.repositories.post_repo_impl import PostRepositoryImpl
from app.infrastructure.repositories.comment_repo_impl import CommentRepositoryImpl
from app.infrastructure.repositories.user_repo_impl import UserRepositoryImpl
from app.usecases.post_service import PostService
from app.usecases.comment_service import CommentService
from app.usecases.user_service import UserService
from app.infrastructure.db.session import SessionLocal


def get_post_service():
    db = SessionLocal()
    repo = PostRepositoryImpl(db)
    return PostService(repo)


def get_comment_service():
    db = SessionLocal()
    repo = CommentRepositoryImpl(db)
    return CommentService(repo)


def get_user_service():
    db = SessionLocal()
    repo = UserRepositoryImpl(db)
    return UserService(repo)
