class Config(object):
    DEBUG = False
    SECRET_KEY = '{using JWT}'
    # CSRF_SESSION_KEY = SESSION_KEY
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    migration_directory = 'migrations'


class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db_dev.db'


class Testing(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db_test.db'


class Production(Config):
    TESTING = False
    DEBUG = False


app_config = {
    'dev': Development,
    'test': Testing,
    'prod': Production
}
