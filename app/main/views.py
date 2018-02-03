from flask import render_template
from . import main
from ..request import get_news,get_details
#views


@main.route('/')
def index():
    '''
    function that returns index page
    '''
    message = 'hello world'
    title = 'the best news website ever'

    general_list = get_news('us', 'general')
    business_list = get_news('us', 'business')
    technology_list = get_news('us', 'technology')
    sports_list = get_news('us', 'sports')
    health_list = get_news('us', 'health')
    science_list = get_news('us', 'science')
    entertainment_list = get_news('us', 'entertainment')
    test_args = 'Working!'
    return render_template('index.html',general=general_list,business=business_list,technology=technology_list,sports=sports_list,health=health_list,science=science_list,entertainment=entertainment_list)
   


# dynamic routes
#bussiness news

# @main.route('/news')
# def news():
#     '''
#     view news details

#     '''
    
#     business = get_news('business')

#     return render_template('news.html',news=news,business=business)


#entertainment news

# @main.route('/entertainment')
# def entertainment():
#     '''
#     view news details

#     '''
#     entertainment= get_news('entertainment')
    
 

#     return render_template('entertainment.html',entertainment=entertainment)


# @main.route('/general')
# def general():
#     '''
#     view news details

#     '''
     
    
#     general= get_news('general')

#     return render_template('general.html',general=general)


# @main.route('/health')
# def health():
#     '''
#     view news details

#     '''
#     health= get_news('health')

#     return render_template('health.html',health=health)

# @main.route('/sport')
# def sport():
#     '''
#     view news details

#     '''
#     sports= get_news('sports')

#     return render_template('sports.html',sports=sports)

# @main.route('/science')
# def science():
#     '''
#     view news details

#     '''
#     science= get_news('science')

#     return render_template('science.html',science=science)

# @main.route('/technology')
# def technology():
#     '''
#     view news details

#     '''
      
#     technology= get_news('technology')


#     return render_template('technology.html',technology=technology)




@main.route('/news/<id>')
def news(id):
    """
    View articles page that returns the news article from a highlight
    """
    news_args = get_details(id)
    highlight_args = 'Route Working!!'
    # name = f'{results_list}'
    return render_template('news.html',highlight_param=highlight_args,news=news_args)

