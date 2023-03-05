import logging
from flask import Blueprint, render_template, request
import utils

main_blueprint = Blueprint('main_blueprint', __name__)
post_blueprint = Blueprint('post_blueprint', __name__)
search_blueprint = Blueprint('search_blueprint', __name__)
user_name_blueprint = Blueprint('user_name_blueprint', __name__)

@main_blueprint.route('/')
def page_index():
    items = utils.get_posts_all()
    return render_template('index.html', items = items)

@post_blueprint.route('/posts/<int:post_id>')
def page_post(post_id):
    post = utils.get_post_by_pk(post_id)
    comments = utils.get_comments_b_post_id(post_id)
    coat = len(comments)
    return render_template('post.html', post = post, comments = comments, coat = coat)

@search_blueprint.route('/search')
def page_search():
    s = request.args['s']
    logging.info('Выполняется поиск')
    items = utils.search_for_posts(s)
    coat = len(items)
    return render_template('search.html', items=items, coat = coat)


@user_name_blueprint.route('/users/<user_name>')
def page_user_name(user_name):
    items =  utils.get_posts_by_user(user_name)
    return render_template('user-feed.html', items = items, user_name = user_name)
