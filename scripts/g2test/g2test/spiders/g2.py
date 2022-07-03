import scrapy
from scrapy.http import Request


class G2Spider(scrapy.Spider):
    name = 'g2'
    allowed_domains = ['g2.com']
    start_urls = ['http://g2.com/']

    """"
    def start_requests(self):
        print('********* START REQUESTS *********')
        headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36'}
        #headers = {}
        for url in self.start_urls:
            yield Request(url, headers=headers)
    """
    
    def parse(self, response):
        pass
