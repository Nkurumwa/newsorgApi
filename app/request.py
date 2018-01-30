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
    source_dictionary = {}
    for news_item in news_list:
        #storing the nested list in source id
        source_id = news_item['source']
        #extract information
        source_dictionary['id'] = source_id['id']
        source_dictionary['name'] = source_id['name']
        id = source_dictionary['id']
        name = source_dictionary['name']
        print(name)
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

def get_details(id):
    get_news_details_url = base_url.format(id,api_key)
    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.load(news_details_data)

        news_object = None

        if news_details_response:
            #storing the nested list in source id
            source_id = news_item['source']
            #extract information
            source_dictionary['id'] = source_id['id']
            source_dictionary['name'] = source_id['name']
            id = source_dictionary['id']
            name = source_dictionary['name']
            print(name)
            author = news_item.get('author')
            title = news_item.get('title')
            description = news_item.get('description')
            url = news_item.get('url')
            urlToImage = news_item.get('urlToImage')
            publishedAt = news_item.get('publishedAt')

            news_object = Articles(id,name,author,title,description,url,urlToImage,publishedAt)
    return news_object
