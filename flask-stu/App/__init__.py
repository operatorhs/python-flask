from flask import Flask
from App.views import init_view
from App.ext import init_ext
from App.settings import envs


def create_app(env):
    app = Flask(__name__)
    # 加载配置文件
    app.config.from_object(envs.get(env))
    # 初始化第三方库
    init_ext(app)
    # 初始化路由
    init_view(app)
    return app

