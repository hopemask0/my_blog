from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.models.user import UserCreate, UserRead
from app.domain.repositories.user_repo import UserRepository
from app.infrastructure.db.models import User as UserModel

class UserRepositoryImpl(UserRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[UserRead]:
        users = self.db.query(UserModel).all()
        return [UserRead.from_orm(user) for user in users]

    def get_by_id(self, user_id: int) -> Optional[UserRead]:
        user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        return UserRead.from_orm(user) if user else None

    def get_by_param(self, **kwargs) -> List[UserRead]:
        users = self.db.query(UserModel).filter_by(**kwargs).all()
        return [UserRead.from_orm(user) for user in users]

    def create(self, user: UserCreate) -> UserRead:
        db_user = UserModel(**user.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return UserRead.from_orm(db_user)
