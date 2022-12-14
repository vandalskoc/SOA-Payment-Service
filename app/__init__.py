import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    @app.template_filter()
    def currencyFormat(value):
        value = float(value)
        return "{:,.2f} VND".format(value)


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,  url_prefix='/auth')

    return app