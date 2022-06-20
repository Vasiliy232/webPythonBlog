from os import getenv


SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    'postgresql+psycopg2://user:password@localhost:5432/blog'
)


class Config:
    ENV = "development"
    TESTING = False
    DEBUG = False
    SECRET_KEY = "fsafdahgjgkjklj"
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    ENV = "production"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    ENV = "testing"
    TESTING = True
