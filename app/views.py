from flask import render_template
from app import app

#views

@app.route('/')
def index():
    '''
    this return the index page
    '''
    title = " hey lewis is back in the business"
    return render_template('index.html', title = title)
@app.route('/news/<int:totalResults>')
def news(totalResults):
    '''
    page function that returns books data

    '''
    return render_template('news.html', id = totalResults)
