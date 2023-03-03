
from exts import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    phone = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(100))
    icon = db.Column(db.String(256))
    isdelete = db.Column(db.Boolean, default=False)
    rdatetime = db.Column(db.DateTime, default=datetime.now)
    articles = db.relationship('Article', backref='user', lazy='dynamic')

    def __str__(self):
        return self.username



