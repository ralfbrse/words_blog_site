from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


# Function called at project execution.
def create_app():

    # app : Instance of Flask
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "beans"

    # imoprt website blueprints
    from .views import views
    from .auth import auth

    # register blueprints in Flask instance
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
