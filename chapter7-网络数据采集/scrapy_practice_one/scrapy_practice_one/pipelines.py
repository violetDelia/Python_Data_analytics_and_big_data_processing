# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyPracticeOnePipeline:
    def process_item(self, item, spider):
        with open("result.txt", "a") as file:
            for i in range(0, len(item["name"])):
                content = "{0}:{1} \n".format(item["name"][i], item["href"][i])
                file.write(content)
