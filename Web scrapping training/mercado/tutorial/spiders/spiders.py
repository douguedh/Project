


import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from mercado.items import MercadoItem
from scrapy.exceptions import CloseSpider

class MercadoSpider(CrawlSpider):
    name = "mercado"
    item_count = 0
    allowed_domain = ["https://www.mercadolivre.com.br/"]
    start_url = ["https://lista.mercadolivre.com.br/celulares#D[A:celulares]"]


rules = {
    # Para cada item
    Rule(LinkExtractor(allow=(), restrict_xpaths = ("//*[@id="root-app"]/div/div[1]/section/div[3]/ul/li[12]/a/span[1]"))),
    Rule(LinkExtractor(allow=(), restrict_xpaths = ("//h2[@class="ui-search-item__title"]"]/a")),
                    callback = "parse_item", follow = False)
    }

    def parse_item(self, response):
        ml_item = MercadoItem()
        ml_item["titulo"] = response.xpath("normalize_space(//h1[@class="ui-pdp-title"])").extract()
        ml_item["folio"] = response.xpath("normalize_space(//span[@class="ui-pdp-subtitle"]))".extract()
        ml_item["condicion"] = response.xpath("normalize_space(//*[@id="root-app"]/div/div[4]/div/div[2]/div[1]/div/div[3]/div/div[1]/div/span[1])").extract()
        ml_item["titulo"] = response.xpath('normalize_space()').extract()
        ml_item["titulo"] = response.xpath('normalize_space()').extract()
        ml_item["titulo"] = response.xpath('normalize_space()').extract()
        ml_item["titulo"] = response.xpath('normalize_space()').extract()
