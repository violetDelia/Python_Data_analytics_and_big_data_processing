# -*- coding: utf-8 -*-
import scrapy

from baidumusic.items import BaidumusicItem
from lxml import etree

class BaidumusicspiderSpider(scrapy.Spider):
    name = 'baidumusicspider'
    allowed_domains = ["music.taihe.com"]
    start_urls = ["http://music.taihe.com/top/new/?pst=shouyeTop"]

    def parse(self, response):
        html = response.text
        html_obj = etree.HTML(html)
        li_list = html_obj.xpath("//div[contains(@class,'song-list song-list-hook')]/ul/li")
        id_list = []
        for li in li_list:
            song_item = BaidumusicItem()
            a_tag = li.xpath("./div/span[@class='song-title ']/a[@href]")
            if a_tag is not None:
                a_href = a_tag[0].attrib["href"]
                song_item["song_id"] = a_href.split("/")[2]
                print(song_item["song_id"])
                id_list.append(song_item)

        return id_list
