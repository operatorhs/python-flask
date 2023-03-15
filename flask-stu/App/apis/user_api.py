
from flask_restful import Resource


class UsersResource(Resource):

    def get(self):
       return {'msg': 'User List'}


class UserResource(Resource):

    def get(self, id):
        return {'msg': 'User%d ok' % id}
