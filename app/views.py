from flask import render_template
from app import app
from  .request import get_news_source
#views

@app.route('/')
def index():
    '''
    this return the index page
    '''

    #getting technology news
    sport = get_news_source('za','sport')
    science = get_news_source('za','science')
    health = get_news_source('za','health')
    entertainment = get_news_source('za','entertainment')
    business = get_news_source('za','business')
    technology = get_news_source('za','technology')
    print(technology)

    title = " hey lewis is back in the business"
    return render_template('index.html', title = title, technology = technology, sport=sport,science=science,health=health,business=business,entertainment=entertainment)
@app.route('/news/<int:totalResults>')
def news(totalResults):
    '''
    page function that returns books data

    '''
    return render_template('news.html', id = totalResults)


