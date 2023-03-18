from flask import Blueprint, request, jsonify, current_app, url_for, render_template, g, flash, redirect
from werkzeug.utils import secure_filename
import os
from ext import csrf, db
from models.post import BoardModel, PostModel, CommentModel
from decorators import login_required
from flask_paginate import Pagination
from forms.post import PublicCommentForm

bp = Blueprint('front', __name__, url_prefix='')


@bp.post('/upload/image')
@csrf.exempt
@login_required
def upload_image():
    f = request.files.get('file')
    extension = f.filename.split('.')[-1].lower()
    if extension not in ['jpg', 'gip', 'png', 'jpeg']:
        return jsonify({
            'errno': 400,
            'data': []
        })

    filename = secure_filename(f.filename)
    f.save(os.path.join(current_app.config.get('UPLOAD_IMAGE_PATH'), filename))
    # url = url_for('media.media_file', filename=filename)
    url = os.path.join('/static', 'upload', filename)
    return jsonify({
        'errno': 0,
        'data': [{
            'url': url,
            'alt': '',
            'href': ''
        }]
    })


@bp.post('/upload/video')
@csrf.exempt
@login_required
def upload_video():
    f = request.files.get('file-video')
    extension = f.filename.split('.')[-1].lower()
    if extension not in ['mp4']:
        return jsonify({
            'errno': 400,
            'message': '您上传的格式不是mp4'
        })
    filename = secure_filename(f.filename)
    f.save(os.path.join(current_app.config.get('UPLOAD_IMAGE_PATH'), filename))
    url = os.path.join('/static', 'upload', filename)
    return jsonify({
        'errno': 0,
        'data': {
            'url': url
        }
    })


@bp.post('/post/<int:post_id>/comment')
@login_required
def post_comment(post_id):
    form = PublicCommentForm(request.form)
    if form.validate():
        content = form.content.data
        comment = CommentModel(content=content, post_id=post_id, author=g.user)

        db.session.add(comment)
        db.session.commit()
    else:
        for message in form.messages:
            flash(message)

    return redirect(url_for('post.post_detail', post_id=post_id))


@bp.route('/')
def index():
    # posts = PostModel.query.all()
    boards = BoardModel.query.all()

    page = request.args.get('page', type=int, default=1)
    board_id = request.args.get('board_id', type=int, default=0)

    start = (page - 1) * current_app.config.get('PER_PAGE_COUNT')
    end = start + current_app.config.get('PER_PAGE_COUNT')

    query_obj = PostModel.query.filter_by(is_active=True).order_by(PostModel.create_time.desc())
    if board_id:
        query_obj = query_obj.filter_by(board_id=board_id)
    total = query_obj.count()

    posts = query_obj.slice(start, end)
    pagination = Pagination(bs_version=4, page=page, total=total, outer_window=0, inner_window=2, alignment='center')

    context = {
       'posts': posts,
        'boards': boards,
        'pagination': pagination,
        'current_board': board_id
    }
    return render_template('front/index.html', **context)
