from forms.baseform import BaseFrom

from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Length


class PublicPostForm(BaseFrom):
    title = StringField(validators=[Length(min=2, max=100, message='请正确长度的标题')])
    content = StringField(validators=[Length(min=2, message='请输入正确长度的内容')])
    board_id = IntegerField(validators=[InputRequired(message='请输入板块id')])


class PublicCommentForm(BaseFrom):
    content = StringField(validators=[Length(min=2, max=200, message='请输入正确长度的评论')])

