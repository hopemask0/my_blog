from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.models.post import PostCreate, PostRead
from app.domain.repositories.post_repo import PostRepository
from app.infrastructure.db.models import Post as PostModel


class PostRepositoryImpl(PostRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[PostRead]:
        posts = self.db.query(PostModel).all()
        return [PostRead.from_orm(post) for post in posts]

    def get_by_id(self, post_id: int) -> Optional[PostRead]:
        post = self.db.query(PostModel).filter(PostModel.id == post_id).first()
        return PostRead.from_orm(post) if post else None

    def get_by_param(self, **kwargs) -> List[PostRead]:
        posts = self.db.query(PostModel).filter_by(**kwargs).all()
        return [PostRead.from_orm(post) for post in posts]

    def create(self, post: PostCreate) -> PostRead:
        db_post = PostModel(**post.dict())
        self.db.add(db_post)
        self.db.commit()
        self.db.refresh(db_post)
        return PostRead.from_orm(db_post)
