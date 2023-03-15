from flask import Blueprint, request, render_template, g
from utils import restful
from decorators import login_required
from forms.post import PublicPostForm

from ext import db

from models.post import BoardModel, PostModel

bp = Blueprint('post', __name__)


@bp.route('/post/public', methods=['GET', 'POST'])
@login_required
def public_post():
    if request.method == 'GET':
        boards = BoardModel.query.all()
        return render_template('front/public_post.html', boards=boards)
    else:
        form = PublicPostForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            board_id = form.board_id.data
            post = PostModel(title=title, content=content, board_id=board_id, author=g.user)
            db.session.add(post)
            db.session.commit()
            return restful.ok()
        else:
            messages = form.messages[0]
            return restful.params_error(message=messages)


@bp.get('/post/detail/<int:post_id>')
def post_detail(post_id):
    post = PostModel.query.get(post_id)
    post.read_count += 1
    db.session.commit()
    return render_template('front/post_detail.html', post=post)














