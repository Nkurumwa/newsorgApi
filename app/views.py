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


# dynamic routes

@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    view news details

    '''

    return render_template('news.html', id = news_id)