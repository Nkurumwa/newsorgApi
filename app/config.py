class Config:
    '''
    general configueation of app
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=&category={}&apiKey={}'

    

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

