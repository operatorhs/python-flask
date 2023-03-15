from flask import Blueprint, render_template, request, current_app, redirect, url_for, flash, session
from ext import cache, db
from utils import restful
import random
from forms.user import RegisterForm, LoginForm
from models.user import UserModel

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('front/register.html')
    else:
        print('===>11', request.form.get('captcha'))
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email, username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.login'))
        else:
            for message in form.messages:
                flash(message)
            return redirect(url_for('user.register'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('front/login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = UserModel.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session['user_id'] = user.id
                if remember:
                    session.permanent = True
                return redirect('/')
            else:
                flash('邮箱或者密码错误')
                return redirect(url_for('user.login'))
        else:
            for message in form.messages:
                flash(message)
            return render_template('front/login.html')


@bp.route('/')
def index():
    return 'index'


@bp.route('/mail/captcha')
def mail_captcha():
    try:
        email = request.args.get('email')
        digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        captcha = ''.join(random.sample(digits, 4))
        subject = '尊敬的懂敏：【知了python论坛】注册验证码'
        body = f'【知了Python论坛】您的注册验证码是：{captcha},请勿告诉别人。'
        # message = Message(subject=subject, recipients=[email], body=body)
        current_app.celery.send_task('send_mail', (email, subject, body))
        cache.set(email, captcha, timeout=100)
        return restful.ok()
    except Exception as e:
        print(e)
        return restful.server_error()


@bp.route('/get_cache')
def get_cache():
    captcha = cache.get('2239537420@qq.com')
    return captcha

