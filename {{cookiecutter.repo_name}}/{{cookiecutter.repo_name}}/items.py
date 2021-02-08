import scrapy


class {{cookiecutter.repo_name_caps}}Item(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    date = scrapy.Field()
