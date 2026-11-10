import pytest
import requests


@pytest.mark.smoke
def test_get_posts_returns_200(base_url):
    response = requests.get(f"{base_url}/posts")
    assert response.status_code == 200


@pytest.mark.regression
def test_get_posts_returns_list(base_url):
    response = requests.get(f"{base_url}/posts")
    assert isinstance(response.json(), list)
    assert len(response.json()) == 100


@pytest.mark.regression
@pytest.mark.parametrize("post_id", [1, 2, 50, 100])
def test_get_single_post_has_expected_fields(base_url, post_id):
    response = requests.get(f"{base_url}/posts/{post_id}")
    body = response.json()
    assert response.status_code == 200
    assert body["id"] == post_id
    assert {"userId", "id", "title", "body"} <= body.keys()


@pytest.mark.regression
@pytest.mark.parametrize("post_id", [0, 101, 9999])
def test_get_nonexistent_post_returns_404(base_url, post_id):
    response = requests.get(f"{base_url}/posts/{post_id}")
    assert response.status_code == 404


@pytest.mark.regression
def test_create_post_returns_201(base_url):
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(f"{base_url}/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == "foo"