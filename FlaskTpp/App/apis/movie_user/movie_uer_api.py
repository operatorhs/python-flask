from flask_restful import Resource


class MovieUserResource(Resource):

    def get(self):
        return {'msg': 'ok'}



