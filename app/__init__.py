from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
#initializing application

app = Flask(__name__,instance_relative_config=True)


#setting up configurations

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')
from app import views

