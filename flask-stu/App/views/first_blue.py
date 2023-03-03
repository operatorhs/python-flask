import os

from flask import Blueprint, render_template
from App.models import User
from App.ext import db

first_blue = Blueprint('blue', __name__)


@first_blue.route('/')
def index():
    return render_template('index.html', msg='这天气适合睡觉')


@first_blue.route('/create_db')
def create_db():

    db.create_all()
    return '创建成功'


@first_blue.route('/add_user')
def add_user():
    user = User()
    user.username = 'Tom'
    db.session.add(user)
    db.session.commit()
    return '添加数据成功'


@first_blue.route('/drop_db')
def drop_user():
    db.drop_all()
    return '删除成功'

