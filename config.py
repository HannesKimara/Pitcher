import secrets

class Config:
    '''
    General configuration parent class
    '''

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:admin@localhost/pitch'
    SECRET_KEY = secrets.token_hex(16)

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True


class TestConfig(Config):
    '''
    Test configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:admin@localhost/pitch_test'

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test': TestConfig,
}
