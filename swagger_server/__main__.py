#!/usr/bin/env python3

import connexion
import os

from flask import Flask
from swagger_server.database import db

from swagger_server.config import config
from swagger_server import encoder


def create_app():
    app = connexion.FlaskApp(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Matter API'}, pythonic_params=True)
    configure_app(app.app, os.getenv('FLASK_CONFIG') or 'default')
    init_app(app.app)
    return app


def init_app(flask_app: Flask):
    db.init_app(flask_app)


def configure_app(flask_app: Flask, config_name: str):
    flask_app.config.from_object(config[config_name])

def main():
    app = create_app()
    app.run(port=8763)


if __name__ == '__main__':
    main()
