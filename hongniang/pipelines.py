# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class HongniangPipeline(object):
    # def __init__(self):
    #     self.filename = open("hongniang.json", "wb")
    #     self.lists = []
    # def process_item(self, item, spider):
    #     content = json.dumps(dict(item), ensure_ascii=False) +",\n"
    #     self.filename.write(content.encode("utf-8"))
    #     #self.lists.append(content.encode("utf-8"))
    #     return item
    #
    # def close_spdier(self, spider):
    #     #self.filename.write(self.lists)
    #     self.filename.close()
    def process_item(self, item, spider):
        # 格林威治时间，距离中国 +8 时区
        # 爬虫名
        item['spidername'] = spider.name
        return item
