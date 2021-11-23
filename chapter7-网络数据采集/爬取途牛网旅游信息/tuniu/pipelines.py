# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TuNiuPipeline(object):
    def process_item(self, item, spider):
        with open("product.txt", "a") as file:
            content = "产品金额：{0}  ,{1}".format(item["promotion"], item["resource_price_save"])
            file.write(content)
