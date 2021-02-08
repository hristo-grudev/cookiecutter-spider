import re

import scrapy

from scrapy.loader import ItemLoader
from ..items import {{cookiecutter.repo_name_caps}}Item
from itemloaders.processors import TakeFirst


class {{cookiecutter.repo_name_caps}}Spider(scrapy.Spider):
	name = '{{cookiecutter.repo_name}}'
	start_urls = ['{{cookiecutter.project_link}}']

	def parse(self, response):
		post_links = response.xpath('//div[@class="post_content"]/a/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

		next_page = response.xpath('//div[@class="pagination pagination__posts"]/ul/li[@class="next"]/a/@href').getall()
		yield from response.follow_all(next_page, self.parse)


	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//article//text()[normalize-space() and not(ancestor::h2 | ancestor::p[@class="date"] | ancestor::a)]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//article/p[@class="date"]/text()').get()

		item = ItemLoader(item={{cookiecutter.repo_name_caps}}Item(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
