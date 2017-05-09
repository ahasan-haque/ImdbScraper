import re
import scrapy
from scrapy.loader import ItemLoader

class IMDBSpider(scrapy.Spider):
    name = "imdb"
    start_urls = ["http://www.imdb.com/chart/top"]

    def parse(self, response):
        for genre_page in response.xpath('//li[@class = "subnav_item_main"]/a/@href').extract():
            genre_page = re.sub(r'(num_votes=)\d+','\g<1>500000',genre_page)
            yield scrapy.Request(response.urljoin(genre_page), callback= self.parse_attributes)

    def parse_attributes(self, response):
        for movie_url in response.xpath('//h3[@class = "lister-item-header"]/a/@href').extract():
            #print movie_url
            yield scrapy.Request(response.urljoin(movie_url), callback=self.fetch_movie)

    def fetch_movie(self, response):
        #print("---------------------------------------------------------------------->")
        print response.xpath('//h1[@itemprop = "name"]/text()').extract_first()
