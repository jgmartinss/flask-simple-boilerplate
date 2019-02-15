from decouple import config


class Config(object):
    SECRET_KEY = config('SECRET_KEY')
    #CSRF_SESSION_KEY = SESSION_KEY
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    migration_directory = 'migrations'


class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = config('DATABASE_PATH')


class Testing(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = config('DATABASE_PATH')


class Production(Config):
    TESTING = False
    DEBUG = False


app_config = {
    'development': Development, 
    'testing': Testing, 
    'production': Production
}


def get_config():
    """Return env class."""
    if config('ENV') == 'dev':
        return app_config['development']
    elif config('ENV') == 'test':
        return app_config['testing']
    elif config('ENV') == 'prod':
        return app_config['production']
