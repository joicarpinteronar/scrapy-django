import scrapy

from app.models import Mercado
from scrapping.items import BlogPostItem
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from mercado.items import MercadoItem

class MercadoSpider(CrawlSpider):
    name = 'mercado'
	item_count = 0
	allowed_domain = ['www.mercadolibre.com.co']
	start_urls = ['https://listado.mercadolibre.com.co/celulares-xiaomi#D[A:celulares%20xiaomi]']

	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//li[@class="andes-pagination__arrow-title"]/a'))),
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//h2[contains(@class,"main-title")]/a')),
							callback = 'parse_item', follow = False)
	}

	def parse_item(self, response):
		ml_item = MercadoItem()
		#info de producto
		ml_item['titulo'] = response.xpath('normalize-space(//h1[@class="item-title__primary"]/text())').extract_first()

		ml_item['precio'] = response.xpath('normalize-space(//span[@class="price-tag-fraction"]/text())').extract()

		ml_item['envio'] = response.xpath('normalize-space(//p[contains(@class, "shipping-method-title shipping-text")]/text())').extract()

        ml_item['vendido'] = response.xpath('normalize-space(//[(@class = "item-conditions")]/text())').extract()

        ml_item['opiniones'] = response.xpath('normalize-space(//span[@class="average-legend"]/text())').extract()
		#imagenes del producto
		ml_item['image_urls'] = response.xpath('//figure[contains(@class, "gallery-image-container")]/a/img/@src').extract()
		ml_item['image_name'] = response.xpath('normalize-space(//h1[@class="item-title__primary "]/text())').extract_first()

		self.item_count += 1
		if self.item_count > 20:
			raise CloseSpider('item_exceeded')
		yield ml_item
