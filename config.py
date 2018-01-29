import os

class Config:
    '''
    general configueation of app
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=&category={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get ('SECRET_KEY')
    

class prodConfig(Config):
    '''
    configs based on the production of the app
    '''
    pass


class devConfig(Config):
    '''
    configurations of development configurations
    '''
    DEBUG = True

config_options = {
    'development':devConfig,
    'production':prodConfig
}

