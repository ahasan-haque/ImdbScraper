# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags



class ImdbItem(scrapy.Item):
    movie_name = scrapy.Field()
    release_date = scrapy.Field()
    rating = scrapy.Field()
    director_name = scrapy.Field()
    writer_name = scrapy.Field()
    metascore = scrapy.Field()
    popularity = scrapy.Field()
    oscars_wins = scrapy.Field()
    other_awards = scrapy.Field()
    nominations = scrapy.Field()
    storyline = scrapy.Field()
    tagline = scrapy.Field()
    genres = scrapy.Field()
    country = scrapy.Field()
    filming_locations = scrapy.Field()
    budget = scrapy.Field()
    gross_income = scrapy.Field()
    production_company = scrapy.Field()
    runtime = scrapy.Field()