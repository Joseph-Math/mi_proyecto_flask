import os
from flask import Flask
from .views import init_views

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_mapping(
        SECRET_KEY='dev-secret-change-me',
        DB_HOST='localhost',
        DB_USER='root',
        DB_PASSWORD='abc123abc123',
        DB_NAME='desarrollo_web',
    )
    init_views(app)
    return app
