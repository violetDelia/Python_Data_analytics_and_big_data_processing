# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BaidumusicPipeline(object):
    def process_item(self, item, spider):
        with open("baidu_music_id_list.txt", "a") as file:
            file.write(item["song_id"] + "\n")


class BaidumusicDetailPipeline(object):
    def process_item(self, item, spider):
        if item is not None:
            with open("baidu_music_detail_list.txt", "a") as file:
                content = "{0},{1},{2},{3},{4}".format(item["song_id"],
                                                       item["song_name"],
                                                       item["artist"],
                                                       item["publish_date"],
                                                       item["company"])
                file.write(content + "\n")
