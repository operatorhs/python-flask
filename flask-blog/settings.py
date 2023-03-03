import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:hs6307609@127.0.0.1:3306/flask_blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'skdjlsfjladfjldfl'

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
    UPLOAD_DIR = os.path.join(STATIC_DIR, 'upload')
    UPLOAD_PHOTO_DIR = os.path.join(STATIC_DIR, 'photo')


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'


class ProductionConfig(Config):
    ENV = False
    DEBUG = False

