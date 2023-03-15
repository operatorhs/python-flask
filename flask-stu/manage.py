
import os
from flask_script import Manager
# from flask_restful import Resource, Api


from flask_migrate import MigrateCommand
from App import create_app

env = os.environ.get('FLASK_ENV', default='develop')


app = create_app(env)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


# api = Api(app)


# class HelloWordResource(Resource):
#     def get(self):
#         return {'hello', 'word'}
#
# api.add_resource()


if __name__ == '__main__':
    manager.run()
