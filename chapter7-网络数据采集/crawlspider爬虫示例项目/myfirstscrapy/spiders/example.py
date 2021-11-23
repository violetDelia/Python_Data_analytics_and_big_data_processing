# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider

from myfirstscrapy.items import NewsItem
from lxml import etree


class ExampleSpider(RedisCrawlSpider):
    name = "meiju"
    allowed_domains = ["www.meijutt.com"]
    redis_key = "meiju:start_urls"

    def parse(self, response):
        html = response.text
        html_obj = etree.HTML(html)
        li_list = html_obj.xpath("//div[@class='l week-hot layout-box']/ul/li")
        for li in li_list:
            news_item = NewsItem()
            news_item["title"] = li.xpath("a/text()")[0]
            yield news_item
