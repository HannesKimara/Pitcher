import secrets, os

class Config:
    '''
    General configuration parent class
    '''

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:admin@localhost/pitch'
    SECRET_KEY = secrets.token_hex(16)

    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_SUPPRESS_SEND = False

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


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
