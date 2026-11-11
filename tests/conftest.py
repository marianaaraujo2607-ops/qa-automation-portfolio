import os

import pytest

from api.posts_client import PostsClient


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")


@pytest.fixture(scope="session")
def posts_client(base_url):
    return PostsClient(base_url)