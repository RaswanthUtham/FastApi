import pytest
from pprint import pprint
from app import schemas

def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")
    # pprint(res.json())
    assert res.status_code == 200
    assert len(res.json()) == len(test_posts)

def test_get_one_post(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].id}")
    post = schemas.PostVote(**res.json())
    assert res.status_code == 200
    assert post.Post.id == test_posts[0].id
    assert post.Post.content == test_posts[0].content
    assert post.Post.title == test_posts[0].title
    assert post.Post.created_at == test_posts[0].created_at

def test_unauthorized_get_all_posts(client, test_posts):
    res = client.get("/posts/")
    # pprint(res.json())
    assert res.status_code == 401

def test_unauthorized_get_one_post(client, test_posts):
    res = client.get("/posts/{test_posts[0].id}")
    assert res.status_code == 401

def test_get_one_post_not_exist(authorized_client, test_posts):
    res = authorized_client.get("/posts/1001")
    assert res.status_code == 404

@pytest.mark.parametrize("title, content, published",[
        ("awesome new title", "awesome new content", True),
        ("chicken Biriyani", "I Love Beef", False),
        ("tallest Lic","Almost true" , True)])
def test_create_post(authorized_client, test_user, test_posts, title, content, published):
    res = authorized_client.post("/posts/", json={"title": title, "content": content, "pblished": published})
    created_post = schemas.PostCreate(**res.json())
    assert res.status_code == 201
    assert created_post.title == title
    assert created_post.content == content

