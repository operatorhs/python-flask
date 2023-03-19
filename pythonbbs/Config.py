from datetime import timedelta
import os


class BaseConfig:
    SECRET_KEY = 'zhi_hui_ke_ji'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    Debug = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:hs6307609@localhost:3306/pythonbbs?charset=utf8'

    # 基本路径设置
    BASE_DIR = os.path.dirname(os.path.abspath(__name__))
    UPLOAD_IMAGE_PATH = os.path.join(BASE_DIR, 'static', 'upload')
    AVATAR_SAVE_PATH = os.path.join(BASE_DIR, 'static', 'avatars')

    # 邮箱配置
    MAIL_SERVER = 'smtp.163.com'
    MAIL_USE_SSL = True
    MAIL_PORT = 465
    MAIL_USERNAME = '18112488219@163.com'
    MAIL_PASSWORD = 'ABJAOMHQSIOBQKIK'
    MAIL_DEFAULT_SENDER = '18112488219@163.com'

    # 缓存配置
    CACHE_TYPE = 'RedisCache'
    CACHE_REDIS_HOST = '127.0.0.1'
    CACHE_REDIS_PORT = 6379

    # Celery 配置
    CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
    CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'

    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

    # 分页配置
    PER_PAGE_COUNT = 10


class TestingConfig(BaseConfig):
    Debug = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:hs6307609@localhost:3306/pythonbbs?charset=utf8'


class StagingConfig(BaseConfig):
    Debug = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:hs6307609@localhost:3306/pythonbbs?charset=utf8'


class ProductionConfig(BaseConfig):
    Debug = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:hs6307609@localhost:3306/pythonbbs?charset=utf8'


if __name__ == '__main__':
    s = os.path.dirname(os.path.abspath(__name__))
    c = os.path.join(s, 'static', 'upload')
    print(c)

