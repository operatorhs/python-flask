from flask_restful import Resource, reqparse, abort, fields, marshal_with

from App.apis.api_constant import HTTP_CREATE_OK, USER_ACTION_LOGIN, USER_ACTION_REGISTER
from App.models.movie_user import MovieUser
from .model_utils import get_user

# 获取参数
parse = reqparse.RequestParser()
parse.add_argument('username', type=str, required=True, location='form', help='请输入用户名')
parse.add_argument('password', type=str, required=True, location='form',  help='请输入密码')
parse.add_argument('phone', type=str, required=True, location='form',  help='请输入手机号码')
parse.add_argument('action', type=str, required=True, location='form', help='请确认请求参数')

movie_user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'password': fields.String(attribute='_password'),
    'phone': fields.String
}

single_movie_user_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.Nested(movie_user_fields)
}


class MovieUsersResource(Resource):

    @marshal_with(single_movie_user_fields)
    def post(self):
        args = parse.parse_args()
        username = args.get('username')
        password = args.get('password')
        phone = args.get('phone')

        action = args.get('action').lower()

        if action == USER_ACTION_REGISTER:

            movie_user = MovieUser(username=username, password=password, phone=phone)
            if not movie_user.save():
                abort(400, mesages='创建失败')
            data = {
                'status': HTTP_CREATE_OK,
                'msg': '用户创建成功',
                'data': movie_user
            }
            return data
        elif action == USER_ACTION_LOGIN:
            user = get_user(username) or get_user(phone)
            if not user:
                abort(400, msg='用户不存在')
            if not user.check_password(password):
                abort('401', message='用户名或者密码错误')

        else:
            abort(400, msg='请提供正确的参数')



