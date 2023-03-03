from flask import Blueprint, render_template, request
from exts import db
from apps.user.models import User
from apps.article.models import Article

article_bp = Blueprint('article', __name__, url_prefix='/article')


@article_bp.route('/publish', methods=['GET', 'POST'])
def publish_article():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        uid = request.form.get('uid')

        article = Article()
        article.title = title
        article.content = content
        article.user_id = uid

        db.session.add(article)
        db.session.commit()
        return '添加文章成功'

    else:
        users = User.query.filter(User.isdelete==False).all()
        print(users)
    return render_template('article/add_article.html', users=users)


@article_bp.route('/all')
def all_article():
    articles = Article.query.all()
    return render_template('article/all.html', articles=articles)


@article_bp.route('/all1')
def all_article1():
    id = request.args.get('id')
    user = User.query.get(id)
    return render_template('article/all.html', articles=user.articles)
