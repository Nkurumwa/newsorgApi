from flask import render_template
from app import app

#views


@app.route('/')
def index():
    '''
    function that returns index page
    '''
    message = 'hello world'

    return render_template('index.html',message=message)