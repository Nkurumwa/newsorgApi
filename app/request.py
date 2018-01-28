from app import app
import urllib.request
from .models import news
import json
News = news.News

#getting api key

api_key = app.config["NEWS_API_KEY"]

#getting the news url

base_url = app.config["NEWS_API_BASE_URL"] 

def get_news_source(category):
    '''
    creating a function that takes in json request to url request
    '''
    get_news_source_url = base_url.format(category,api_key)
    
    with urllib.request.urlopen(get_news_source_url) as url:
        get_news_source_data = url.read()
        get_news_source_response = json.loads(get_news_source_data)
        # print(get_news_source_response)

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
        print(url)
        urlToImage = source_item.get('urlToImage')
        
        publishedAt = source_item.get('publishedAt')

        if urlToImage:
            source_object = News(name,auther,title,description,url,urlToImage,publishedAt)
            source_result.append(source_object)

    return source_result


# a function to get all the news details 

def get_news_details(title):
    get_news_details_url = base_url.format(title,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_detail_response = json.load(news_details_data)
        print(news_detail_response)

        news_object = None

        if news_detail_response:
            auther = news_detail_response.get('author')
            name = news_detail_response.get('name')
            title = news_detail_response.get('title')
            description = news_detail_response.get('description')
            url = news_detail_response.get('url')
            urlToImage = news_detail_response.get('urlToImage')
            publishedAt = news_detail_response.get('publishedAt')
                
            news_object = News(name,auther,title,description,url,urlToImage,publishedAt)

    return news_object

# function to display the news detals