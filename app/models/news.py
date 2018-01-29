class News:
    '''
    defining news object
    '''

    def __init__(self,name,auther,title,description,url,urlToImage,publishedAt):
        self.name = name
        self.auther = auther
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
