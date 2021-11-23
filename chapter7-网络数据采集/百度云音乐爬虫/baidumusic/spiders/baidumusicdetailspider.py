# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from lxml import etree

from baidumusic.items import BaidumusicDetailItem


class BaidumusicdetailspiderSpider(scrapy.Spider):
    name = 'baidumusicdetailspider'
    allowed_domains = ['music.taihe.com']
    start_urls = ['http://music.taihe.com/']

    def start_requests(self):
        with open("baidu_music_id_list.txt", "r") as file:
            for song_id in file:
                url = "http://music.taihe.com/song/{0}".format(song_id.strip())
                yield Request(url, dont_filter=True)

    def parse(self, response):
        html = response.text
        html_obj = etree.HTML(html)
        div = html_obj.xpath("//div[contains(@class,'song-info-box fl')]")
        song_name = div[0].xpath("./h2/span/text()")[0]
        artist = div[0].xpath("./p[@class='artist-box']/span/span/a/text()")[0]
        publish_date = div[0].xpath("./p[@class='publish desc']/text()")[0]
        company = div[0].xpath("./p[@class='company desc']/text()")[0]

        detail_item = BaidumusicDetailItem()
        detail_item["song_id"] = response.url.split("/")[-1]
        detail_item["song_name"] = song_name
        detail_item["artist"] = artist
        detail_item["publish_date"] = publish_date
        detail_item["company"] = company
        return detail_item
