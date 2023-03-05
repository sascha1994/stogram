import json


def get_posts_all():
    with open('data/posts.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_posts_by_user(user_name):
    names = []
    for name in get_posts_all():
        if user_name == name['poster_name']:
            names.append(name)
    if len(names) == 0:raise ValueError('Такого пользователя нет')
    return names


def get_comments_b_post_id(post_id):
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        comments = []
        data = json.load(file)
        for comment in data:
            # if post_id != comment['post_id']: raise ValueError('Такого поста нет')
            if post_id == comment['post_id']:
                comments.append(comment)
        return comments


def get_post_by_pk(pk):
    for post in get_posts_all():
        if pk == post['pk']:
            return post

def search_for_posts(query):
    posts = []
    for content in get_posts_all():
        post = content['content'].split()
        post = [x.lower() for x in post]
        for i in range(len(post)):
            f = filter(str.isalpha, post[i])
            post[i] = "".join(f)
        if query in post:
            posts.append(content)
    return posts




# get_posts_all() - возвращает посты
# get_posts_by_user(user_name) - возвращает посты определенного пользователя. Функция
# должна вызывать ошибку valueError если такого пользователя нет и пустой список, если у
# пользователя нет постов.
# get_comments_by„post_id(post_id) - возвращает комментарии определенного поста.
# Функция должна вызывать ошибку ValueError если такого поста нет и пустой список, если у
# поста нет комментов.
# search_for_posts(query) - возвращает список постов по ключевому слову
# get_post_by_pk(pk) - возвращает один пост по его идентификатору.
