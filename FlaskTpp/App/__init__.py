from flask import Flask
from App.settings import envs


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(envs.get(env))
    return app

