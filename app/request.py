from app  import app
import urllib.request,json
from .models import news
Articles=news.Articles

#get api key

api_key = app.config['NEWS_API_KEY']

#get news base url 

base_url = app.config['NEWS_API_KEY_URL']

def get_news(category):
    '''
    function of getting json response ro url
    '''
    get_news_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_result = None


        if get_news_response['articles']:
            news_result_list = get_news_response['articles']
            news_result = process_results(news_result_list)

    return news_result

def process_results(news_list):
    '''
    function that takes in the movie results and transform them to a list
    '''
    news_result =[]
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')

        if urlToImage:
            news_object = Articles(id,name,author,title,description,url,urlToImage,publishedAt)
            news_result.append(news_object)
    return news_result

