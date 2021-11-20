"""
This files contains the request and response structures.
"""

from pydantic import BaseModel
from datetime import datetime

from pydantic.networks import EmailStr

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    created_at: datetime
    id: int

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserPost(BaseModel):
    email: EmailStr
    
    class Config:
        orm_mode = True