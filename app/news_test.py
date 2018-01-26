import unittest
from models import news
News = news.News

class Booktest(unittest.TestCase):
    '''
    test behaviour of the news

    '''

    def setUp(self):
        '''

        '''


        self.new_news = News('Npr.org', 'Colin Dwyer', 'This Mummified Woman Now Has A Name — And A Famous Relative: Boris Johnson','Meet Anna Catharina Bischoff, an 18th-century syphilitic woman found in 1975. Researchers announced her name Thursday. And the U.K. foreign secretary says hes "very proud" to have the new family tie.','https://www.npr.org/sections/thetwo-way/2018/01/25/580670694/this-mummified-woman-now-has-a-name-and-a-famous-relative-boris-johnsonurlimage','https://media.npr.org/assets/img/2018/01/25/2017_barfuesser_mumie12686-1-_wide-ad997bac67a1ce57496ec170addac04863a5e32a.jpg?s=1400',20180125205900)
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
if __name__ == '__main__':
    unittest.main()