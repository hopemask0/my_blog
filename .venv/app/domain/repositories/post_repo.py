from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.models.post import PostCreate, PostRead

class PostRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[PostRead]:
        pass

    @abstractmethod
    def get_by_id(self, post_id: int) -> Optional[PostRead]:
        pass

    @abstractmethod
    def get_by_param(self, **kwargs) -> List[PostRead]:
        pass

    @abstractmethod
    def create(self, post: PostCreate) -> PostRead:
        pass
