# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titulo = scrapy.Field()
    folio = scrapy.Field()
    precio = scrapy.Field()
    condicion = scrapy.Field()
    envio = scrapy.Field()
    ubicaccion = scrapy.Field()
    opiniones = scrapy.Field()
    ventas_producto = scrapy.Field()
    
    
    #info de la tienda o vendedor
    vendedor_url = scrapy.Field()
    tipo_vendedor = scrapy.Field()
    reputacion = scrapy.Field()
    ventas_vendedor = scrapy.Field()
    pass
