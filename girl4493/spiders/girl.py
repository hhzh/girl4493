# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from girl4493.items import Girl4493Item


class GirlSpider(scrapy.Spider):
    name = "girl"
    # allowed_domains = ["4493.com"]
    start_urls = ['https://www.4493.com']

    def parse(self, response):
        count = 0
        for sel in response.xpath('//li/a[@target="_blank"]'):
            item = Girl4493Item()
            item['title'] = sel.xpath('span/text()').extract_first(default='not found')
            item['package_url'] = 'https://www.4493.com' + sel.xpath('@href').extract_first(default='not found')
            count = count + 1
            item['name'] = str(count) + '.jpg'
            if item['title'] != 'not found' and item['package_url'] != 'not found':
                yield scrapy.Request(url=item['package_url'], meta={'item': item}, callback=self.parse_detail,
                                     dont_filter=True)

    def parse_detail(self, response):
        item = response.meta['item']
        pic_url = response.xpath('//div[@class="picsbox picsboxcenter"]/p/img/@src').extract_first(default='not found')
        if pic_url != 'not found':
            item['pic_url'] = pic_url
            # response.xpath('//div[@class="page"]')
            yield item
            # for sel in response.xpath('//li[@class="hover"]/a[@target="_blank"]'):
            #     item['title'] = sel.xpath('p[@class="tit"]/text()').extract_first(default='not found')
            #     item['package_url'] = 'https://www.4493.com' + sel.xpath('@href').extract_first(default='not found')
            #     yield Request(item['package_url'], callback=self.parse)
