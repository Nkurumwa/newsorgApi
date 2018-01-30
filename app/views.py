from flask import render_template
from app import app
from .request import get_news,get_details
#views


@app.route('/')
def index():
    '''
    function that returns index page
    '''
    message = 'hello world'
    title = 'the best news website ever'

    #get article categories
   
   
    
    
   
  

    return render_template('index.html',message=message,title=title)



# dynamic routes
#bussiness news

@app.route('/news')
def news():
    '''
    view news details

    '''
    
    business = get_news('business')

    return render_template('news.html',news=news,business=business)


#entertainment news

@app.route('/entertainment')
def entertainment():
    '''
    view news details

    '''
    entertainment= get_news('entertainment')
    
 

    return render_template('entertainment.html',entertainment=entertainment)


@app.route('/general')
def general():
    '''
    view news details

    '''
     
    
    general= get_news('general')

    return render_template('general.html',general=general)


@app.route('/health')
def health():
    '''
    view news details

    '''
    health= get_news('health')

    return render_template('health.html',health=health)

@app.route('/sport')
def sport():
    '''
    view news details

    '''
    sports= get_news('sports')

    return render_template('sports.html',sports=sports)

@app.route('/science')
def science():
    '''
    view news details

    '''
    science= get_news('science')

    return render_template('science.html',science=science)

@app.route('/technology')
def technology():
    '''
    view news details

    '''
      
    technology= get_news('technology')


    return render_template('technology.html',technology=technology)



