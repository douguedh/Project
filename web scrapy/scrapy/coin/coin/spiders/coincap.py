import scrapy
from ..items import ProductItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

class CoincapSpider(scrapy.Spider):
    name = 'coincap'
    allowed_domains = ['coinmarketcap.com']
    start_urls = ['https://coinmarketcap.com/currencies']
    
    rules = (
        Rule(LinkExtractor(allow=('/'), restrict_css=('.cmc-link')),
            callback="parse_item", follow=True),)
    
    def parse(self, response):
        product = response.xpath('//td')
        for p in product:
            position = p.css('.sc-13jrx81-0 YxBdW cmc-label cmc-label--success::text').extract_first()
            name = p.xpath(
                '//div[@class="cmc-details-panel-header__name"]/h1/text()').get()
            sigla = p.xpath(
                '//div[@class="cmc-details-panel-header__name"]/h1/span/text()').get()
            price = p.xpath(
                '///span[@class="cmc-details-panel-price__price"]/text()').get()
            marketcap = p.xpath(
                '//ul[@class="sc-15acgj0-0 dyvdrp cmc-details-panel-stats"]/li[1]/div[1]/span[1]/text()').get()
            item = ProductItem()
            item['Position'] = position
            item['Name'] = name
            item['Sigla'] = sigla
            item['Price'] = price
            item['marketcaptotal'] = marketcap
            yield item


