import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts_returns_200():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200