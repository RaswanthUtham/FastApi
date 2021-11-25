import pytest
from fastapi.testclient import TestClient
from pprint import pp, pprint
from app import models
from app.database import get_db
from app.main_orm import app
from app.database import Base
from app.oauth2 import create_access_token
from .database import engine, TestingSessionLocal

@pytest.fixture(scope="function")
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture(scope="function")
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)

@pytest.fixture
def test_user(client):
    user_data = {"email": "magizhan_01@gmail.com", "password": "test@123"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user

@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user['id']})

@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }
    return client

@pytest.fixture
def test_posts(test_user, session):
    posts_data = [
        {
            "title": "1st post",
            "content": "No problem",
            "owner_id": test_user["id"]
        },
        {
            "title": "2nd post",
            "content": "Be Happy",
            "owner_id": test_user["id"]
        },
        {
            "title": "3rd post",
            "content": "No Stress",
            "owner_id": test_user["id"]
        }
    ]
    posts = [models.Post(**x) for x in posts_data]
    session.add_all(posts)
    # session.add_all(
    #     [
    #         models.Post(title="1st post", content="No problem", owner_id=test_user["id"]),
    #         models.Post(title="2nd post", content="Be Happy", owner_id=test_user["id"]),
    #         models.Post(title="3rd post", content="No Stress", owner_id=test_user["id"]),
    #     ]
    # )
    session.commit()
    session.query(models.Post).all()
    return posts

