# -*- coding: utf-8 -*-
import scrapy
from lxml import etree

from tuniu.items import TourismItem


class TuNiuSpider(scrapy.Spider):
    name = "tuniuspider"
    allowed_domains = ["www.tuniu.com"]
    url = """http://www.tuniu.com/package/210740698?source=bb&ta_pst=%E5%88%86%E7%B1%BB%E9%A1%B5_%E5%87%BA%E5%A2%83%E6%97%85%E6%B8%B8-%E9%A9%AC%E5%B0%94%E4%BB%A3%E5%A4%AB_1&ad_id=210740698"""
    start_urls = [url]

    def parse(self, response):
        html = response.text
        html_obj = etree.HTML(html)
        item = TourismItem()
        item["promotion"] = html_obj.xpath(
            "//div[@class='resource-section-content']/span[@class='price-quantity']/span[@class='price-number']/text()")[
            0]
        item["resource_price_save"] = \
            html_obj.xpath("//span[@id='J_ResourcePromotionPriceTip']/span[@class='resource-price-save']/text()")[0]
        print(item)