import os


def get_db_uri(dbinfo):
    engine = dbinfo.get('ENGINE') or 'sqlite'
    driver = dbinfo.get('DRIVER') or 'sqlite'
    user = dbinfo.get('USER') or 'root'
    password = dbinfo.get('PASSWORD') or 'hs6307609'
    host = dbinfo.get('HOST') or '127.0.0.1'
    port = dbinfo.get('PORT') or '3306'
    name = dbinfo.get('NAME') or 'tpp'
    # mysql+pymysql://root:hs6307609@127.0.0.1:3306/gpi
    return f'{engine}+{driver}://{user}:{password}@{host}:{port}/{name}'


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'dsafasdfasdfkla'

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class DevelopmentConfig(Config):
    DEBUG = True
    dbinfo = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'hs6307609',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'flask_tpp'
    }
    # mysql+pymysql://root:hs6307609@127.0.0.1:3306/gpi
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class TestingConfig(Config):
    DEBUG = False
    dbinfo = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'hs6307609',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'gpi'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)




class StagingConfig(Config):
    DEBUG = False
    dbinfo = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'hs6307609',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'gpi'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class ProductionConfig(Config):
    DEBUG = False
    dbinfo = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'hs6307609',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'gpi'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


envs = {
    'develop': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
