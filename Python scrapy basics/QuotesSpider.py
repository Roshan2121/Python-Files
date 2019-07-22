import scrapy
from ..items import ScraperItem

class scraper(scrapy.Spider):

	name = "spider"
	start_urls = ["http://quotes.toscrape.com/"]

	def parse(self, response):        # css XPATH or regex selectors.

		container = ScraperItem()
		infos = response.css('div.quote')

		quote = infos.css('span.text::text').extract()
		written_by = infos.css('small.author::text').extract()

		container['quote'] = quote
		container['written_by'] = written_by

		yield container
