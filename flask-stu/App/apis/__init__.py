from flask_restful import Resource, Api

# from App.apis.user_api import UsersResource, UserResource
from App.apis.hello_api import HelloResource
from App.apis.goods import GoodsListResource, GoodsResource
api = Api()


def init_api(app):
    api.init_app(app)


# api.add_resource(UsersResource, '/api_user/')
# api.add_resource(UserResource, '/api_user/<int:id>/')

api.add_resource(HelloResource, '/')
api.add_resource(GoodsListResource, '/goods/')
api.add_resource(GoodsResource, '/goods/<int:id>/', endpoint='sign_goods')
