# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyfirstscrapyPipeline(object):
    def process_item(self, item, spider):
        with open("yao_wen.txt", "a") as file:
            file.write(item["title"] + "\n")
