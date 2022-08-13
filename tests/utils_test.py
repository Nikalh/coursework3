import pytest

from utils import get_posts_all, get_comments_by_post_id, get_posts_by_user


@pytest.fixture()
def data():
    return get_posts_all()


def test_get_posts_all(data):
    """Возвращаем посты"""
    assert get_posts_all() == data


def test_get_posts_by_user():
    """Возвращаем посты определенного пользователя. Вызываем ошибку ValueError
    если такого пользователя нет и пустой список, если у пользователя нет постов"""
    assert get_posts_by_user("larry")


def test_get_comments_by_post_id():
    """Возвращает комментарии определенного поста. Вызываем ошибку ValueError
    если такого поста нет и пустой список, если у поста нет комментов"""
    assert get_comments_by_post_id(1)

# print(get_comments_by_post_id())pytest
