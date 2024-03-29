from flask import Flask
from flask_migrate import Migrate
import Config
from ext import db, mail, cache, csrf, avatars
from blueprints import init_view
from bbs_celery import make_celery
# from flask_wtf import CSRFProtect
import commands
import filters
import hooks


from models.user import PermissionEnum, PermissionModel, RoleModel
from models import user

app = Flask(__name__)
app.config.from_object(Config.DevelopmentConfig)

db.init_app(app)
migrate = Migrate(app, db)
mail.init_app(app)
cache.init_app(app)
celery = make_celery(app)
# CSRFProtect(app)
csrf.init_app(app)
avatars.init_app(app)

app.template_filter('email_hash')(filters.email_hash)

init_view(app)

# 添加钩子函数
app.before_request(hooks.bbs_before_request)
app.errorhandler(404)(hooks.bbs_404_error)
app.errorhandler(401)(hooks.bbs_401_error)
app.errorhandler(500)(hooks.bbs_500_error)
# 添加命令
app.cli.command('my-command')(commands.my_command)
app.cli.command('create-permission')(commands.create_permission)
app.cli.command('create-role')(commands.create_role)
app.cli.command('create-test-user')(commands.create_test_user)
app.cli.command('create-admin')(commands.create_admin)
app.cli.command('create-board')(commands.create_board)
app.cli.command('create-test-post')(commands.create_test_post)


if __name__ == '__main__':
    # print(app.import_name)
    app.run(debug=True)
