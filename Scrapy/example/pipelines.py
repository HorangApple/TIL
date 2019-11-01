# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime
from example.items import Article
from string import whitespace


class ExamplePipeline(object):
    def process_item(self, item, spider):
        # 항목별로 처리할 수 있도록 if와 isinstance 사용
        if isinstance(item,Article):
            dateStr = item['lastUpdated']
            dateStr = dateStr.replace('This page was last edited on', '')
            dateStr = dateStr.strip()
            dateStr = datetime.strptime(dateStr, '%d %B %Y, at %H:%M')
            dateStr = dateStr.strftime('%Y-%m-%d %H:%M:%S')
            item['lastUpdated'] = dateStr

            texts = item['text'][0:50]
            texts = [line for line in texts if line not in whitespace]
            item['text'] = ''.join(texts)

            return item
