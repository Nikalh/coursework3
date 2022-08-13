import json
import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request, jsonify

from utils import search_for_posts, get_post_by_pk, get_posts_all, get_comments_by_post_id, get_posts_by_user

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    posts: list[dict] = get_posts_all()
    return render_template('index.html', posts=posts)


# print(main_page())
# создаем блюпринт для поиска и ловим ошибки, ведем лог
@main_blueprint.route('/search/')
def search_page():
    search_query = request.args.get('s', '')
    logging.info('Выполняю поиск')
    try:
        posts = search_for_posts(search_query)

    except FileNotFoundError:
        return "Файл не найден"
    except JSONDecodeError:
        return "Не валидный файл"
    return render_template('search.html', posts=posts)


@main_blueprint.route('/post/<int:idx>')
def post_page(idx):
    logging.info('Выполняю поиск')
    try:
        posts: list[dict] = get_post_by_pk(idx)
        comments = get_comments_by_post_id(idx)
    except FileNotFoundError:
        return "Файл не найден"
    except JSONDecodeError:
        return "Не валидный файл"
    return render_template('post.html', comments=comments, posts=posts)


@main_blueprint.route('/post/')
def post_pages():
    logging.info('Выполняю поиск')
    try:
        posts: list[dict] = get_posts_all()

    except FileNotFoundError:
        return "Файл не найден"
    except JSONDecodeError:
        return "Не валидный файл"
    return render_template('post.html', posts=posts)


# print(post_page(1))

@main_blueprint.route('/users/<user_name>')
def user_post_page(user_name):
    logging.info('Выполняю поиск')
    try:
        post = get_posts_by_user(user_name)
    except FileNotFoundError:
        return "Файл не найден"
    except JSONDecodeError:
        return "Не валидный файл"
    return render_template('user-feed.html', post=post)


@main_blueprint.route('/api/posts/')
def api_page():
    logging.info('Выполняю поиск')
    posts: list[dict] = get_posts_all()
    return jsonify(posts)
#

@main_blueprint.route('/api/posts/<int:pk>')
def get_api_posts_by_pk(pk):
    posts = get_post_by_pk(pk)
    logging.info('Выполняю поиск')
    return jsonify(posts)


# @main_blueprint.route('/tag/<word>')
# def user_tag_page(word):
#     logging.info('Выполняю поиск')
#     try:
#         post = search_tag_posts('#', word)
#     except FileNotFoundError:
#         return "Файл не найден"
#     except JSONDecodeError:
#         return "Не валидный файл"
#     return render_template('tag.html', post=post)
