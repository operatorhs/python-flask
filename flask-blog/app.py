from apps import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate

from exts import db

from apps.user.models import User
from apps.article.models import *
from apps.goods.models import *

app = create_app()
manager = Manager(app=app)
migrate = Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    manager.run()
