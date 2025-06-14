from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str
    user_id: int

class PostCreate(PostBase):
    pass

class PostRead(PostBase):
    id: int
    model_config = {"from_attributes": True}
