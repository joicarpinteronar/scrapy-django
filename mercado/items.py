# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from app.models import Mercado

class MercadoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #informacion del producto
    titulo = scrapy.Field()
    precio = scrapy.Field()
    envio = scrapy.Field()
    vendido = scrapy.Field()
    opiniones = scrapy.Field()


    #imagenes
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_name = scrapy.Field()

class MercadoItem(DjangoItem):

    django_model = Mercado
