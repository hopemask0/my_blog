from typing import List, Optional
from app.domain.models.user import UserCreate, UserRead
from app.domain.repositories.user_repo import UserRepository

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def get_all_users(self) -> List[UserRead]:
        return self.repo.get_all()

    def get_user_by_id(self, user_id: int) -> Optional[UserRead]:
        return self.repo.get_by_id(user_id)

    def get_users_by_param(self, **kwargs) -> List[UserRead]:
        return self.repo.get_by_param(**kwargs)

    def create_user(self, user: UserCreate) -> UserRead:
        return self.repo.create(user)
