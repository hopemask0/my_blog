from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.models.user import UserCreate, UserRead

class UserRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[UserRead]:
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[UserRead]:
        pass

    @abstractmethod
    def get_by_param(self, **kwargs) -> List[UserRead]:
        pass

    @abstractmethod
    def create(self, user: UserCreate) -> UserRead:
        pass
