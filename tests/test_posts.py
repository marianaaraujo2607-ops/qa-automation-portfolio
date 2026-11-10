import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts_returns_200():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200

def test_get_posts_returns_list():
    response = requests.get(f"{BASE_URL}/posts")
    assert isinstance(response.json(), list)
    assert len(response.json()) == 100

def test_get_single_post_has_expected_fields():
    response = requests.get(f"{BASE_URL}/posts/1")
    body = response.json()
    assert response.status_code == 200
    assert {"userId", "id", "title", "body"} <= body.keys()

def test_get_nonexistent_post_returns_404():
    response = requests.get(f"{BASE_URL}/posts/9999")
    assert response.status_code == 404

def test_create_post_returns_201():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == "foo"