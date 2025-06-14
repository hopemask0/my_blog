from pydantic import BaseModel

class CommentBase(BaseModel):
    post_id: int
    content: str
    user_id: int

class CommentCreate(CommentBase):
    pass

class CommentRead(CommentBase):
    id: int
    model_config = {"from_attributes": True}
