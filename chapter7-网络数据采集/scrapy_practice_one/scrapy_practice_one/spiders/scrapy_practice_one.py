import scrapy
from lxml import etree
from scrapy_practice_one.items import scrapy_practice_oneItem


class scrapy_practice_oneSpider(scrapy.Spider):
    name = 'scrapy_practice_one'
    allowed_domains = ['www.ooee.top/']
    start_urls = ['https://www.ooee.top/']

    def parse(self, response):
        html = response.text
        html_obj = etree.HTML(html)
        item = scrapy_practice_oneItem()
        

        href_attrbute= html_obj.xpath("//*[@id='content']/div[7]/*/div/a[1][@href]")
        href_list = []
        for i in href_attrbute:
            href_list.append(i.attrib['href'])
        item["href"] =href_list
        name_attrbute=html_obj.xpath("//*[@id='content']/div[7]/div/div/a[1]/div/div/div[1]/img[@alt]")
        name_list= []
        for i in name_attrbute:
            name_list.append(i.attrib['alt'])
        item["name"] =name_list
        print(item)
        return item

