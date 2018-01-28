from flask import render_template
from app import app
from  .request import get_news_source,get_news_details
#views

@app.route('/')
def index():
    '''
    this return the index page
    '''

    #getting technology news
    sport = get_news_source('sport')
    science = get_news_source('science')
    health = get_news_source('health')
    entertainment = get_news_source('entertainment')
    business = get_news_source('business')
    technology = get_news_source('technology')
    print(technology)

    title = " hey lewis is back in the business"
    return render_template('index.html', title = title, technology = technology, sport=sport,science=science,health=health,business=business,entertainment=entertainment)
@app.route('/news/<title>')
def news(title):
    '''
    page function that returns books data

    '''
    news = get_news_details(title)
    title = f(source_result.title)

    return render_template('news.html',title = title)


