# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaidumusicItem(scrapy.Item):
    song_id = scrapy.Field()


class BaidumusicDetailItem(scrapy.Item):
    song_id = scrapy.Field()
    song_name = scrapy.Field()
    artist = scrapy.Field()
    publish_date = scrapy.Field()
    company = scrapy.Field()

