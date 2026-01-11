from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, Literal

from pydantic.types import conint


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

from pydantic import ConfigDict

class Config:
    model_config = ConfigDict(from_attributes=True)



class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
from pydantic import BaseModel, ConfigDict

class MySchema(BaseModel):
    ...
    model_config = ConfigDict(from_attributes=True)



class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)