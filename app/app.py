import os

from flask import Flask

def create_flask_app():
    app = Flask(__name__)

    app.env_vars = os.environ

    return app

flask_app = create_flask_app()
