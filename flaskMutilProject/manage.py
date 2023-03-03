from flask_script import Manager

from App import crate_app

app = crate_app('develop')

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
