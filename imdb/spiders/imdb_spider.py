import re
import scrapy
from scrapy.loader import ItemLoader
from imdb.items import ImdbItem
from imdb.utils.contentpath import name_to_xpath_mapper


class IMDBSpider(scrapy.Spider):
    name = "imdb"
    start_urls = ["http://www.imdb.com/chart/top"]

    def parse(self, response):
        for genre_page in response.xpath('//li[@class = "subnav_item_main"]/a/@href').extract():
            genre_page = re.sub(r'(num_votes=)\d+', '\g<1>100000', genre_page)
            yield scrapy.Request(response.urljoin(genre_page), callback=self.parse_attributes)

    def parse_attributes(self, response):
        for movie_url in response.xpath('//h3[@class = "lister-item-header"]/a/@href').extract():
            yield scrapy.Request(response.urljoin(movie_url), callback=self.fetch_movie)

    def fetch_movie(self, response):
        item_loader = ItemLoader(item=ImdbItem(), response=response)

        for name, xpath in name_to_xpath_mapper.items():
            item_loader.add_xpath(name, xpath)

        yield item_loader.load_item()
        next_page = response.xpath('//div[@class = "nav"]/div[@class = "desc"]/a/@href').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback= self.fetch_movie)
