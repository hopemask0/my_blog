from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.models.comment import CommentCreate, CommentRead
from app.domain.repositories.comment_repo import CommentRepository
from app.infrastructure.db.models import Comment as CommentModel


class CommentRepositoryImpl(CommentRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[CommentRead]:
        comments = self.db.query(CommentModel).all()
        return [CommentRead.from_orm(comment) for comment in comments]

    def get_by_id(self, comment_id: int) -> Optional[CommentRead]:
        comment = self.db.query(CommentModel).filter(CommentModel.id == comment_id).first()
        return CommentRead.from_orm(comment) if comment else None

    def get_by_param(self, **kwargs) -> List[CommentRead]:
        comments = self.db.query(CommentModel).filter_by(**kwargs).all()
        return [CommentRead.from_orm(comment) for comment in comments]

    def create(self, comment: CommentCreate) -> CommentRead:
        db_comment = CommentModel(**comment.dict())
        self.db.add(db_comment)
        self.db.commit()
        self.db.refresh(db_comment)
        return CommentRead.from_orm(db_comment)
