from typing import List, Optional
from app.domain.models.comment import CommentCreate, CommentRead
from app.domain.repositories.comment_repo import CommentRepository


class CommentService:
    def __init__(self, repo: CommentRepository):
        self.repo = repo

    def get_all_comments(self) -> List[CommentRead]:
        return self.repo.get_all()

    def get_comment_by_id(self, comment_id: int) -> Optional[CommentRead]:
        return self.repo.get_by_id(comment_id)

    def get_comments_by_param(self, **kwargs) -> List[CommentRead]:
        return self.repo.get_by_param(**kwargs)

    def create_comment(self, comment: CommentCreate) -> CommentRead:
        return self.repo.create(comment)
