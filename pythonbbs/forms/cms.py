from .baseform import BaseFrom
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import Email, InputRequired


class AddStaffForm(BaseFrom):
    email = StringField(validators=[Email(message='请输入正确格式的邮箱')])
    role = IntegerField(validators=[InputRequired(message='请选择角色')])


class EditStaffForm(BaseFrom):
    is_staff = BooleanField(validators=[InputRequired(message='请选择是否为员工')])
    role = IntegerField(validators=[InputRequired(message='请选择分组')])
