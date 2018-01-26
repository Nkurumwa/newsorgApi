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
    technology_source = get_news_source('za','technology')
    print(technology_source)

    title = " hey lewis is back in the business"
    return render_template('index.html', title = title, technology_source = technology_source)
@app.route('/news/<int:totalResults>')
def news(totalResults):
    '''
    page function that returns books data

    '''
    return render_template('news.html', id = totalResults)


