# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class ScrapyCnblogsPipeline(object):
    def __init__(self):
        self.file = open("cnblogs.json", "w+")

    def process_item(self, item, spider):
        print(item)
        # 此处如果有中文的话，要加上ensure_ascii=False参数，否则中文乱码,禁止转为ascii编码格式
        record = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(record)
        return item
