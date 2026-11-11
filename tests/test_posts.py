import pytest


@pytest.mark.smoke
def test_get_posts_returns_200(posts_client):
    response = posts_client.list_posts()
    assert response.status_code == 200


@pytest.mark.regression
def test_get_posts_returns_list(posts_client):
    body = posts_client.list_posts().json()
    assert isinstance(body, list)
    assert len(body) == 100


@pytest.mark.regression
@pytest.mark.parametrize("post_id", [1, 2, 50, 100])
def test_get_single_post_has_expected_fields(posts_client, post_id):
    response = posts_client.get_post(post_id)
    body = response.json()
    assert response.status_code == 200
    assert body["id"] == post_id
    assert {"userId", "id", "title", "body"} <= body.keys()


@pytest.mark.regression
@pytest.mark.parametrize("post_id", [0, 101, 9999])
def test_get_nonexistent_post_returns_404(posts_client, post_id):
    response = posts_client.get_post(post_id)
    assert response.status_code == 404


@pytest.mark.regression
def test_create_post_returns_201(posts_client):
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = posts_client.create_post(payload)
    assert response.status_code == 201
    assert response.json()["title"] == "foo"