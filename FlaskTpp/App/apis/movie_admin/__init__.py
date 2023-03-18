from flask_restful import Api

movie_client_api = Api()


def init_app(app):
    movie_client_api.init_app(app)

