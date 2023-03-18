from flask_restful import Api
from .movie_uer_api import MovieUsersResource

client_api = Api(prefix='/user')


def init_app(app):
    client_api.init_app(app)


client_api.add_resource(MovieUsersResource, '/movieusers/')

