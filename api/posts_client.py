import requests


class PostsClient:
    def __init__(self, base_url, timeout=10):
        self.base_url = base_url
        self.timeout = timeout

    def list_posts(self):
        return requests.get(f"{self.base_url}/posts", timeout=self.timeout)

    def get_post(self, post_id):
        return requests.get(f"{self.base_url}/posts/{post_id}", timeout=self.timeout)

    def create_post(self, payload):
        return requests.post(f"{self.base_url}/posts", json=payload, timeout=self.timeout)