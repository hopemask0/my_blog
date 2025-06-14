from typing import List, Optional
from app.domain.models.post import PostCreate, PostRead
from app.domain.repositories.post_repo import PostRepository

class PostService:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def get_all_posts(self) -> List[PostRead]:
        return self.repo.get_all()

    def get_post_by_id(self, post_id: int) -> Optional[PostRead]:
        return self.repo.get_by_id(post_id)

    def get_posts_by_param(self, **kwargs) -> List[PostRead]:
        return self.repo.get_by_param(**kwargs)

    def create_post(self, post: PostCreate) -> PostRead:
        return self.repo.create(post)
