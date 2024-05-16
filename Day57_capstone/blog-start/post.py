import requests


class Post:
    def __init__(self):
        self.blog_url = "https://api.npoint.io/c790b4d5cab58020d391"

    def blog(self):
        blog_response = requests.get(url=self.blog_url)
        blog_response.raise_for_status()
        blog_data = blog_response.json()
        return blog_data
