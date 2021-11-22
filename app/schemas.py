"""
This files contains the request and response structures.
"""

from pydantic import BaseModel
from datetime import datetime
from pydantic.networks import EmailStr
from typing import Optional

from pydantic.types import conint

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserPost(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Posts(PostBase):
    created_at: datetime
    id: int
    owner_id: int
    owner: UserPost

    class Config:
        """ to avoid this error "value is not a valid dict (type=type_error.dict)" """
        orm_mode = True

class PostVote(BaseModel):
    Post: Posts
    votes: int
    class Config:
        """ to avoid this error "value is not a valid dict (type=type_error.dict)" """
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)