from flask import render_template
from app import app
from .request import get_news
#views


@app.route('/')
def index():
    '''
    function that returns index page
    '''
    message = 'hello world'
    title = 'the best news website ever'

    #get article categories
    business = get_news('business')
    entertainment= get_news('entertainment')
    general= get_news('general')
    health= get_news('health')
    science= get_news('science')
    sports= get_news('sports')
    technology= get_news('technology')


    return render_template('index.html',message=message,title=title,business=business,entertainment=entertainment,general=general,health=health,science=science,sports=sports,technology=technology)



# dynamic routes

@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    view news details

    '''

    return render_template('news.html', id = news_id)