"""Class-based Flask app configuration."""
import os
import urllib.parse

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Configuration from environment variables."""
    FLASK_ENV = "development"
    FLASK_APP = "wsgi.py"

    DB_CONFIG_DEV = {
        'db_type': 'sqlite',
        'db_file': 'matter.db'
    }

    DB_CONFIG_STAGE = {
        'db_type': 'postgresql+psycopg2',
        'db_server': 'localhost',
        'db_database': 'avengers',
        'db_username': 'postgres',
        'db_port': '5432',
        'db_password': '*******'
    }

    DB_CONFIG_PROD = {
        'db_type': 'mssql+pyodbc',
        'db_driver': '{ODBC Driver 17 for SQL Server}',
        'db_server': 'alpsql02.alpenland.local',
        'db_database': 'datapool01',
        'db_username': 'sapserviceloc',
        'db_port': '1433',
        'db_password': '*******'
    }


    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    # database
    SQLALCHEMY_DATABASE_URI = '{}:///{}'.format(
        Config.DB_CONFIG_DEV['db_type'],
        Config.DB_CONFIG_DEV['db_file']
    )


class StagingConfig(Config):
    DEBUG = True
    
    SQLALCHEMY_DATABASE_URI = '{}:///{}'.format(
        Config.DB_CONFIG_DEV['db_type'],
        Config.DB_CONFIG_DEV['db_file']
    )


class ProductionConfig(Config):

    SQLALCHEMY_DATABASE_URI = '{}:///{}'.format(
        Config.DB_CONFIG_DEV['db_type'],
        Config.DB_CONFIG_DEV['db_file']
    )

config = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
