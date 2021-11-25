from pydantic.types import Json
from jose import jwt
import pytest
from app import schemas
from app.config import settings

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

def test_login_user(test_user, client):
    res = client.post("/login", data={"username": test_user['email'], "password": test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user["id"]
    assert login_res.token_type == "bearer"
    assert res.status_code == 200
