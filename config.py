import os

class Config:
    '''
    Configuration parent class
    '''
    NEWS_API_BASE_URL =  'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    '''
    production configuration class
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration class
    '''
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}    
    