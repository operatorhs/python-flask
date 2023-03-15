from ext import db
from datetime import datetime


class BoardModel(db.Model):
    __tablename__ = 'board'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.now())
    is_active = db.Column(db.Boolean, default=True)

    posts = db.relationship('PostModel', back_populates='board')


class PostModel(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())
    read_count = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'))
    author_id = db.Column(db.String(100), db.ForeignKey('user.id'), nullable=False)

    board = db.relationship('BoardModel', back_populates='posts')
    author = db.relationship('UserModel', back_populates='posts')
    # comments = db.relationship('CommentModel', back_populates='post')


class CommentModel(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    is_active = db.Column(db.Boolean, default=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    author_id = db.Column(db.String(100), db.ForeignKey('user.id'), nullable=False)

    post = db.relationship('PostModel', backref=db.backref('comments', order_by=create_time.desc()))
    author = db.relationship('UserModel', back_populates='comments')
