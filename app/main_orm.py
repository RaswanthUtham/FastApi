from fastapi import FastAPI, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import AsyncContextManager, Optional, List

from starlette.status import HTTP_201_CREATED

from . import models, schemas, utils
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/posts", response_model=List[schemas.Post])
async def get_posts(db: Session=Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
async def create_post(post: schemas.PostCreate, db: Session=Depends(get_db)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return  new_post

@app.get("/posts/{id}", response_model=schemas.Post)
async def get_post_by_id(id: int, db: Session=Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} not found")
    return post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post_by_id(id: int, db: Session=Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} not found")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}", response_model=schemas.Post)
async def update_post_by_id(id: int, post: schemas.PostCreate, db: Session=Depends(get_db)):
    update_post = db.query(models.Post).filter(models.Post.id == id)
    if not update_post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} not found")
    update_post.update(post.dict(), synchronize_session=False)
    db.commit()
    return update_post.first()

@app.post("/users", status_code=HTTP_201_CREATED, response_model=schemas.UserPost)
async def create_user(user: schemas.UserCreate, db:Session=Depends(get_db)):
    user.password = utils.hash(user.password)
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/users", response_model=List[schemas.UserPost])
async def get_users(db: Session=Depends(get_db)):
    posts = db.query(models.User).all()
    return posts
