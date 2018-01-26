from app import app
import urllib.request
from .models import news
import json
News = news.News

#getting api key

api_key = app.config["NEWS_API_KEY"]

#getting the news url

base_url = app.config["NEWS_API_BASE_URL"] 

def get_news_source(country,category):
    '''
    creating a function that takes in json request to url request
    '''
    get_news_source_url = base_url.format(country,category,api_key)
    
    with urllib.request.urlopen(get_news_source_url) as url:
        get_news_source_data = url.read()
        get_news_source_response = json.loads(get_news_source_data)
        print(get_news_source_response)

        source_result = None

        if get_news_source_response['articles']:
            source_result_list = get_news_source_response['articles']
            source_result = process_result(source_result_list)

    return source_result


def process_result(source_list):
    '''
    this function processes the results and converts them into a list 
    the source list is  a list of dictionaries containing news results
    ''' 
    source_result= []
    for source_item in source_list:
        auther = source_item.get('author')
        name = source_item.get('name')
        title = source_item.get('title')
        description = source_item.get('description')
        url = source_item.get('url')
        urlToImage = source_item.get('urlToImage')
        publishedAt = source_item.get('publishedAt')

        if urlToImage:
            source_object = News(name,auther,title,description,url,urlToImage,publishedAt)
            source_result.append(source_object)

    return source_result


