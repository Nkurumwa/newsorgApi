from flask import Flask
from .config import devConfig
from flask_bootstrap import Bootstrap

#initialize applicatin
app = Flask(__name__,instance_relative_config=True)


#setting up config

app.config.from_object(devConfig)
app.config.from_pyfile('config.py')

#initalizing bootstrap

bootstap=Bootstrap(app)
from app import views