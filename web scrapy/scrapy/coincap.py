from scrapy import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor 
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose

class coincapItem(Item):
    position = Field()
    name = Field()
    siglas = Field()
    price = Field()
    marketcap  = Field()
    volume24 = Field()
    supplycirculation = Field()
    totalsupply = Field()
    maxsupply = Field()
    
class coincapCrawler(CrawlSpider):
    name = "firstcoincrawler"
    start_urls = ['https://coinmarketcap.com', 'https://coinmarketcap.com/2']
    allowed_domais = ['coinmarketcap.com']

    rules = (
            Rule(LinkExtractor(allow=r'/currencies'), callback = 'parse_items'),
    )
    
    def parse_items(self, response):
        item = ItemLoader(coincapItem(), response)
        item.add_xpath('position', '//*[@id="__next"]/div[1]/div[2]/div[1]/div[2]/div[1]/ul[2]/li[1]/span/text()')
        item.add_xpath('name', '//*[@id="__next"]/div[1]/div[2]/div[1]/div[2]/div[1]/div/div[1]/h1/text()')
        item.add_xpath('siglas', '//*[@id="__next"]/div[1]/div[2]/div[1]/div[2]/div[1]/div/div[1]/h1/span/text()[2]')
        item.add_xpath('price', '//*[@id="__next"]/div[1]/div[2]/div[1]/div[2]/div[1]/div/div[2]/span[1]/span[1]/text()')
        item.add_xpath('marketcap', '//*[@id="__next"]/div[1]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[1]/div/span[1]/text()')
        item.add_xpath('volume24', '//*[@id="__next"]/div[1]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[2]/div/span[1]/text()')
        item.add_xpath('supplycirculation', '//*[@id="__next"]/div[1]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[3]/div/div/text()')
        item.add_xpath('totalsupply', '//*[@id="__next"]/div[1]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[4]/div/text()')
        item.add_xpath('maxsupply', '//*[@id="__next"]/div[1]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[5]/div/text()')
        yield item.load_item()
