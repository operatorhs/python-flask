from blueprints.cms import bp as cms_bp
from blueprints.front import bp as front_bp
from blueprints.user import bp as user_bp
from blueprints.post import bp as post_bp
from blueprints.media import bp as media_bp


def init_view(app):
    app.register_blueprint(cms_bp)
    app.register_blueprint(front_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(post_bp)
    app.register_blueprint(media_bp)

