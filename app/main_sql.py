# from operator import pos
import psycopg2
from psycopg2.extras import RealDictCursor
from typing import Optional, final, List
from fastapi import FastAPI, status, HTTPException, Response
from fastapi.params import Body
from random import randrange
from . import schemas

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='toortoor', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection is Successful")
        break
    except Exception as e:
        print("Connection Failed")
        print("Error: ", e)

@app.get("/")
async def root():
    return {"message": "Welcome to my API!! Montize your Knowledge."}

@app.get("/posts", response_model=schemas.Post)
async def get_posts():
    cursor.execute("SELECT * FROM posts")
    my_posts = cursor.fetchall()
    # return {"data": my_posts}
    return my_posts

@app.get('/posts/latest', response_model=List[schemas.Post])
async def get_latest_post():
    cursor.execute("SELECT * FROM posts ORDER BY created_at DESC LIMIT 1;")
    post = cursor.fetchone()
    # return {"Data": post}
    return post

@app.get("/posts/{id}", response_model=schemas.Post)
async def get_post(id: int):
    cursor.execute("SELECT * FROM posts WHERE id = %s", (str(id)))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"string with {id} not found")
    # return {"post": post}
    return post

@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
async def create_posts(payload: schemas.PostCreate):
    cursor.execute("INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *", 
    (payload.title, payload.content, payload.published))
    post_dict = cursor.fetchone()
    conn.commit()
    # return {"new post": post_dict}
    return post_dict

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    cursor.execute("DELETE FROM posts WHERE id = %s RETURNING *", (str(id)))
    deleted_post = cursor.fetchone()
    conn.commit()
    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="tried to delete the post that is not available")
    # return {'message': 'post was successfully deleted'}
    # return my_posts
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}", response_model=schemas.Post)
async def update_post(id: int, post: schemas.PostCreate):
    cursor.execute("UPDATE posts SET title = %s, content = %s, created_at = NOW() WHERE id = %s RETURNING *", (post.title, post.content, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    if not updated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="tried to delete the post that is not available")
    # return {"data": updated_post}
    return update_post