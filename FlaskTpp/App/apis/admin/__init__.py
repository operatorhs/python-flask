from flask_restful import Api

admin_api = Api()


def init_app(app):
    admin_api.init_app(app)



