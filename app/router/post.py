from fastapi import FastAPI, Depends, status, HTTPException, Response, APIRouter
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/posts")

@router.get("/", response_model=List[schemas.Post])
async def get_posts(db: Session=Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
async def create_post(post: schemas.PostCreate, db: Session=Depends(get_db)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return  new_post

@router.get("/{id}", response_model=schemas.Post)
async def get_post_by_id(id: int, db: Session=Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} not found")
    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post_by_id(id: int, db: Session=Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} not found")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.Post)
async def update_post_by_id(id: int, post: schemas.PostCreate, db: Session=Depends(get_db)):
    update_post = db.query(models.Post).filter(models.Post.id == id)
    if not update_post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} not found")
    update_post.update(post.dict(), synchronize_session=False)
    db.commit()
    return update_post.first()