from wtforms import StringField, ValidationError, BooleanField
from wtforms.validators import Email, Length, EqualTo
from ext import cache
from models.user import UserModel
from .baseform import BaseFrom


class RegisterForm(BaseFrom):
    email = StringField(validators=[Email(message='请输入正确的邮箱格式')])
    captcha = StringField(validators=[Length(min=4, max=4, message='请输入正确的验证码格式')])
    username = StringField(validators=[Length(min=2, max=20, message='请输入正确长度的用户名')])
    password = StringField(validators=[Length(min=6, max=20, message='请输入正确长度的密码')])
    confirm_password = StringField(validators=[EqualTo('password', message='两次输入的密码不一致')])

    def validate_email(self, field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise ValidationError(message='邮箱已经存在')

    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        cache_captcha = cache.get(email)
        print('======>', field, email, captcha, cache_captcha )
        if not cache_captcha or captcha != cache_captcha:
            raise ValidationError(message='验证码错误')


class LoginForm(BaseFrom):
    email = StringField(validators=[Email(message='请输入正确格式的邮箱')])
    password = StringField(validators=[Length(min=6, max=20, message='请输入正确长度的密码！')])
    remember = BooleanField()
