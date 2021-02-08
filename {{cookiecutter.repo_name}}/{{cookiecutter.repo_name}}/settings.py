BOT_NAME = '{{cookiecutter.repo_name}}'

SPIDER_MODULES = ['{{cookiecutter.repo_name}}.spiders']
NEWSPIDER_MODULE = '{{cookiecutter.repo_name}}.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'{{cookiecutter.repo_name}}.pipelines.{{cookiecutter.repo_name_caps}}Pipeline': 100,

}