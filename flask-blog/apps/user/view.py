
from flask import Blueprint, render_template, request, redirect, url_for
import hashlib

from sqlalchemy import or_, and_

from exts import db
from .models import User


user_bp = Blueprint('user', __name__)


@user_bp.route('/index')
def index():
    return 'Hello Index'


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        if password != repassword:
            return '两次输入的密码不一致'
        user = User()
        user.username = username
        user.password = hashlib.sha256(password.encode()).hexdigest()
        user.phone = phone
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user.user_center'))
    return render_template('user/register.html')


@user_bp.route('/')
def user_center():
    users = User.query.filter(User.isdelete == False).all()
    return render_template('user/center.html', users=users)


@user_bp.route('/login',  methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        new_password = hashlib.sha256(password.encode()).hexdigest()
        user_list = User.query.filter_by(username=username)
        print(user_list)
        for u in user_list:
            print(u)
            if u.password == new_password:
                return '用户登录成功'
        else:
            return render_template('user/login.html', msg='用户名或者密码有误')

    return render_template('user/login.html')


@user_bp.route('/test_first')
def test_first():
    username = request.args.get('username')
    user = User.query.filter_by(username=username).first()
    print(user.rdatetime)
    return '测试第一条'


@user_bp.route('/select')
def user_select():
    user = User.query.get(1)  # 根据主键查询用户
    # user_list = User.query.filter(or_(User.username.like('z%'), User.username.contains('i'))).all()、
    # __gt__, __lt__, __ge__,
    # user_list = User.query.filter(and_(User.username.contains('s'), User.rdatetime.__lt__('2023-02-12 16:02:30'))).all()
    user_list = User.query.offset(1).limit(1)
    return render_template('user/select.html', user=user, user_list=user_list)

"""
User.username.startswith('')
User.username.endswith('')
User.username.contains('')
User.username.like('')
User.username.in_('')
User.username == 'zzz'
如果要检索的字段是整型状
User.age.__lt__(18) le 小于等于
User.rdatetime.__gt__('.....') ge 大于等于
User.age.between(15, 30)
and_, or_, not_

order_by(rdatetime) 默认升序 需要加.all rdatetime
limit(2) 获取两条数据 offset
"""


@user_bp.route('/search')
def search():
    keyword = request.args.get('search')
    users = User.query.filter(or_(User.username.contains(keyword), User.phone.contains(keyword)))

    return render_template('user/center.html', users=users)


@user_bp.route('/delete')
def delete():
    id = request.args.get('id')
    user = User.query.get(id)
    # 逻辑删除就是删除
    user.isdelete = True
    db.session.commit()
    # 物理删除
    # db.session.delete(user)
    # db.session.commit()
    return redirect(url_for('user.user_center'))


@user_bp.route('/update', endpoint='update', methods=['GET', 'POST'])
def update():

    if request.method == 'POST':
        id = request.form.get('id')
        username = request.form.get('username')
        phone = request.form.get('phone')
        user = User.query.get(id)
        user.username = username
        user.phone = phone
        user.id = id
        db.session.commit()
        return redirect(url_for('user.user_center'))
    else:
        id = request.args.get('id')
        user = User.query.get(id)
        return render_template('user/update.html', user=user)
