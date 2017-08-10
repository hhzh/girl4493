# -*- coding: utf-8 -*-
import scrapy


class GirlSpider(scrapy.Spider):
    name = "girl"
    allowed_domains = ["4493.com"]
    start_urls = ['http://4493.com/']

    def parse(self, response):
        pass
