import pytest
from app import schemas
from .database import client, session

def test_root(client):
    res = client.get("/")
    print(res.json().get('message'))
    assert res.json().get('message') == 'Welcome to my API!! Montize your Knowledge. And Just do it'
    assert res.status_code == 200

def test_create_user(client):
    res = client.post("/users/", json={"email": "magizhan_01@gmail.com", "password": "test@123"})
    user = schemas.UserPost(**res.json())
    assert user.email == "magizhan_01@gmail.com"
    assert res.status_code == 201

def test_login_user(client):
    res = client.post("/login", data={"username": "magizhan_01@gmail.com", "password": "test@123"})
    assert res.status_code == 200
