from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.models.comment import CommentCreate, CommentRead

class CommentRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[CommentRead]:
        pass

    @abstractmethod
    def get_by_id(self, comment_id: int) -> Optional[CommentRead]:
        pass

    @abstractmethod
    def get_by_param(self, **kwargs) -> List[CommentRead]:
        pass

    @abstractmethod
    def create(self, comment: CommentCreate) -> CommentRead:
        pass
