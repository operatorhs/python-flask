from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import settings

from apps.user.models import User
from exts import db
import os

user_bp = Blueprint('users', __name__, url_prefix='/users')


required_login_list = ['/users/center', '/users/update', '/users/publish']


@user_bp.before_app_first_request
def first_request():
    print('before_app_first_request')


@user_bp.after_app_request
def after_request(response):
    print('after_app_request')
    response.set_cookie('a', 'bbbb', max_age=19)
    return response


@user_bp.before_app_request
def first_request():
    print('before_app_request', request.path)
    if request.path in required_login_list:
        print('需要验证的用户的登录状况')
        id = session.get('uid')
        if not id:
            return render_template('users/login.html')
        else:
            user = User.query.get(id)
            g.user = user


# @user_bp.teardown_app_request
# def teardown_request():
#     print('teardown_request')


@user_bp.route('/')
def index1():
    # uid = request.cookies.get('uid', None)
    uid = session.get('uid', None)
    if uid:
        user = User.query.get(uid)
        # paginate(page=1, per_page=3)
        return render_template('users/index.html', user=user)

    return render_template('users/index.html')


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        pass_w = request.form.get('password')
        re_password = request.form.get('re_password')
        phone = request.form.get('phone')
        email = request.form.get('email')

        if pass_w != re_password:
            return '两次输入的密码不一致'

        password = generate_password_hash(pass_w)

        user = User()
        user.username = username
        user.password = password
        user.phone = phone
        user.email = email

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.index'))

    return render_template('users/register.html')


# 手机号码验证
@user_bp.route('/check_phone', methods=['GET', 'POST'])
def check_phone():
    phone = request.args.get('phone')
    users = User.query.filter(User.phone == phone).all()

    # code: 400 不能用  200可以用
    if len(users) != 0:
        return jsonify(code=400, msg='此手机号已经被注册')
    else:
        return jsonify(code=200, msg='此手机号可以用')


@user_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        users = User.query.filter(User.username==username).all()
        for user in users:
            # 是否匹配
            flag = check_password_hash(user.password, password)
            if flag:
                # response = redirect(url_for('users.index1'))
                # response.set_cookie('uid', str(user.id), max_age=1800)
                # return response
                session['uid'] = user.id
                return redirect(url_for('users.index1'))
            else:
                return render_template('users/login.html', msg='用户名或者密码有误')

    return render_template('users/login.html')


@user_bp.route('/login_phone', methods=['POST', 'GET'])
def login_phone():
    if request.method == 'POST':
        phone = request.form.get('phone')
        code = request.form.get('code')
        return redirect(url_for('users.index1'))
    return render_template('users/login.html')


@user_bp.route('/logout', methods=['POST', 'GET'])
def logout():
    # response = redirect(url_for('users.index1'))
    # response.delete_cookie('uid')
    # del session['uid']

    session.clear()
    return redirect(url_for('users.index1'))


# 发送短信
@user_bp.route('/send_msg')
def send_msg():
    pass

# 蓝图钩子函数
# before_app_first_request
# before_app_request
# after_app_request
# teardown_app_request


@user_bp.route('/center')
def user_center():
    print(g.user)
    return render_template('users/center.html', user=g.user)


@user_bp.route('/update', methods=['GET', 'POST'])
def user_change():
    if request.method == 'POST':
        # phone
        # avatar
        phone = request.form.get('phone')
        file = request.files.get('avatar')
        print('====>', file)
        filename = file.filename
        suffix = filename.rsplit('.')[-1]
        ALLOWED_EXTENSIONS = ['png', 'jpg']
        if suffix in ALLOWED_EXTENSIONS:
            filename = secure_filename(filename)  # 保证文件名是符合python 规则的
            file.save(os.path.join(settings.Config.UPLOAD_DIR, filename))
            user = g.user
            path = 'upload'
            user.icon = os.path.join(path, filename)
            db.session.commit()
        else:
            return '上传附件失败'

        # file.save(os.path.join('./upload', 'a.png'))
        return '文件上传成功'

        # users = User.query.all()
        # for user in users:
        #     if user.phone == phone:
        #         # 说明该手机号已经被使用了
        #         return render_template('users/center.html', user=g.user, msg="此号码已经被注册")

    return render_template('users/center.html', user=g.user)


@user_bp.route('/publish', methods=['GET', 'POST'])
def publish():
    if request.method == 'POST':
        pass
    pass
