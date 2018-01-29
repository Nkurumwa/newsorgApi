from flask import render_template
from app import app
from  .request import get_news_source,get_news_details,search_news
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
@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    page function that returns books data

    '''
    # news = get_news_details(title)
    # title = f'{source_result.title}'

    return render_template('news.html',id = news_id)


@app.route('/news/<int:news_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('news.html',id = news_id)


@app.route('/seach/<news_title>')
def search(news_title):
    '''
    functions to display the search results
    '''
    news_name_list = news_title.split("")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for (news_title)'

    return render_template('search.html' news = searched_news )
