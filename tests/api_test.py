import pytest

import main
from config import DATA_PATH_POSTS

key_data = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count",
            "pk"}

class Test_api:

    @pytest.fixture
    def app_instance(self):
        app = main.app
        app.config["DATA_PATH_POSTS"] = DATA_PATH_POSTS
        test_client = app.test_client()

        return test_client

    def test_post_page(self, app_instance):
        result = app_instance.get("/api/posts", follow_redirects=True)
        assert result.status_code == 200, "Неправильный статус "


    def test_page_post_pk(self, app_instance):
        result = app_instance.get("/api/posts/1", follow_redirects=True)
        assert result.status_code == 200, "Неправильный статус "
