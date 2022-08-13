import json

from pathlib import Path

data_path = Path('data', 'data.json')


def get_posts_all() -> list[dict]:
    """Возвращаем посты"""
    with open(data_path, 'r', encoding='utf-8') as file:
        return json.load(file)


# print(get_posts_all())


def get_posts_by_user(user_name):
    """Возвращаем посты определенного пользователя. Вызываем ошибку ValueError
    если такого пользователя нет и пустой список, если у пользователя нет постов"""
    users_posts = get_posts_all()
    try:
        for post in users_posts:

            if user_name.lower() == post["poster_name"].lower():
                return post
    except ValueError:
        return "Пользователь отсутствует"


# print(get_posts_by_user("larry"))


def get_comments_by_post_id(post_id) -> dict:
    """Возвращает комментарии определенного поста. Вызываем ошибку ValueError
    если такого поста нет и пустой список, если у поста нет комментов"""
    comment_path = Path('data', 'comments.json')
    with open(comment_path, 'r', encoding='utf-8') as file:
        posts_comments = json.load(file)

    try:
        result = []
        for comment in posts_comments:
            if post_id == comment["post_id"]:
                result.append(comment)
        return result
    except ValueError:
        return "Комментарий не найден"


# print(get_comments_by_post_id(1))


def search_for_posts(query) -> list[dict]:
    """Возвращает список постов по ключевому слову"""
    result = []
    for post in get_posts_all():
        if query.lower() in post['content'].lower():
            result.append(post)
    return result


def get_post_by_pk(pk) -> list[dict]:
    """Возвращает один пост по его идентификатору"""
    result = []
    for post in get_posts_all():
        if int(pk) == post['pk']:
            result.append(post)
    return result

# print(get_post_by_pk(5))
