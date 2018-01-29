from flask import Flask
from .config import devConfig
from flask_bootstrap import Bootstrap
from config import config_options

bootstap = Bootstrap()

def create_app(config_options):
    app = Flask(__name__)
    #creating the app configurations
        app.config.from_object(config_options[config_name])


    #initializing bootstrap
    bootstap.init_app(app)

    return app