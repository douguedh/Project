import scrapy
from scrapy import item
from ..items import ProductItem

class SportdirectSpider(scrapy.Spider):
    name = 'sportdirect'
    allowed_domains = ['es.sportsdirect.com']
    start_urls = ['https://es.sportsdirect.com/mens/clothing/fleeces']

    def parse(self, response):
        products = response.css('.s-productthumbbox')
        for p in products:
            brand = p.css('.productdescriptionbrand::text').extract_first()
            info_name = p.css('.productdescriptionname::text').extract_first()
            price = p.css('.curprice::text').extract_first()
            item = ProductItem()
            item['Brands'] = brand
            item['Information'] = info_name
            item['Price'] = price
            yield item
        nextPageLinkSelector = response.css('.NextLink::attr(href)')
        if nextPageLinkSelector:
            nextPageLink = nextPageLinkSelector[0].extract()
            yield scrapy.Request(url=response.urljoin(nextPageLink))