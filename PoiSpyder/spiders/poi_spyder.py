import scrapy
import re
from scrapy.http import Request

def parse_item(response):
    pass
class poi_spyder(scrapy.Spider):
    name = "poi"
    start_urls = ["http://travel.qunar.com/p-cs299914-beijing-jingdian-3-1"]

    def parse(self, response):
        url = response.url
        #景点详情页
        if(re.match(r"", url)):
            yield parse_item(response)
        #景点列表页
        elif(re.match(r"", url)):
            yield Request(url, callback=self.parse)


