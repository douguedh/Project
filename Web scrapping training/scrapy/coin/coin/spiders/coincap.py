import scrapy
from ..items import ProductItem

class CoincapSpider(scrapy.Spider):
    name = 'coincap'
    allowed_domains = ['coinmarketcap.com']
    start_urls = ['https://coinmarketcap.com']
    
    
    def parse(self, response):
        product = response.xpath('//td')
        for p in product:
            position = p.xpath('//tbody/tr/td[2]/p/text()').get()
            name = p.xpath(
                '//div[@class="sc-16r8icm-0 sc-1teo54s-1 lgwUsc"]/p/text()').getall()
            sigla = p.xpath('//tbody/tr/td[3]/a/div/div/div/p/text()').getall()
            price = p.xpath(
                '//tbody/tr/td[4]/div/a/text() and //tbody/tr[12]/td[2]/p/text()').getall()
            volaty24 = p.xpath('//tbody/tr/td[5]/span/text()').get()
            volaty7d = p.xpath('//tbody/tr/td[6]/div/span/text()').get()
            marketcap = p.xpath('//tbody/tr/td[7]/p/text()').get()
            volum24 = p.xpath('//tbody/tr/td[8]/div/a/p/text()').get()
            item = ProductItem()
            item['Position'] = position
            item['Name'] = name
            item['Sigla'] = sigla
            item['Price'] = price
            item['volatilidade24'] = volaty24
            item['volatilidade7d'] = volaty7d
            item['marketcaptotal'] = marketcap
            item['volume24'] = volum24
            yield item
