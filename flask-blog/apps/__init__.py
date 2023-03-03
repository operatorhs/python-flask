from flask import Flask
from exts import db, bootstrap
from apps.article.view import article_bp
from apps.user.views import user_bp
from apps.goods.view import goods_bp

import settings


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings.DevelopmentConfig)
    db.init_app(app=app)
    bootstrap.init_app(app=app)

    app.register_blueprint(user_bp)
    app.register_blueprint(article_bp)
    app.register_blueprint(goods_bp)

    # print(app.url_map)

    return app



