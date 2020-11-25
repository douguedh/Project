# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Position = scrapy.Field()
    Name = scrapy.Field()
    Sigla = scrapy.Field()
    Price = scrapy.Field()
    volatilidade24 = scrapy.Field()
    volatilidade7d = scrapy.Field()
    marketcaptotal = scrapy.Field()
    volume24 = scrapy.Field()
