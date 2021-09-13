import unittest
from app.models import News, Articles
#News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test class for testing the behaviour of the news class
    '''
    def setUp(self):
        '''
        setup method to run before the test
        '''
        self.new_news = News('abc', 'Education', 'Education levsl and fundamentals', 'https://study.com/academy/lesson/what.html', 'kenya')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))
        
        
        
class ArticlesTest(unittest.TestCase):
    '''
    Test class for testing the behaviour of articles
    '''        
    def setUp(self):
        self.new_articles = Articles('The strength of the Brain', 'The composition of the brain cells', 'https://images.medicinenet.com/images/image_collection/webmd_anatomy/brain-anatomy.jpg', '19/12/2021 18:06', 'Dr.kinyae', 'https://www.medicinenet.com/image-collection/brain_picture/picture.htm')
        
    def test_instance(self):
            self.assertTrue(isinstance(self.new_articles, Articles))
        
        
 
