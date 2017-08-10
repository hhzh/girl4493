# -*- coding: utf-8 -*-
import os
from urllib import request
from girl4493.items import Girl4493Item

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Girl4493Pipeline(object):
    def __init__(self):
        self.urls_seen = set()

    def process_item(self, item, spider):
        try:
            if item['pic_url'] in self.urls_seen:
                raise Girl4493Item("Duplicate item found: %s" % item)
            else:
                self.urls_seen.add(item['pic_url'])
                request.urlretrieve(item['pic_url'],os.path.join('d:/img/',item['name']))
                return item
        except:
            print('这张图片不能下载', item['name'], item['pic_url'])
