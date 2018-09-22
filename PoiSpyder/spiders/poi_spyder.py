import scrapy
import re
from scrapy.http import Request
from PoiSpyder.items import PoispyderItem

def my_strip(string):
    return ' '.join(string.split())

def list_to_string(word_list):
    string = ""
    for word in word_list:
        string += word
    return string

def my_bytes(string):
    return bytes(string, encoding="utf-8")

def parse_item(response):
    name = response.xpath('//h1[@class="tit"]/text()').extract_first()
    parent_str = response.xpath('//div[@class="ranking"]/text()').extract_first()
    parent = parent_str.split('景点排名')[0]
    parent_rank = response.xpath('//div[@class="ranking"]/span[@class="sum"]/text()').extract_first()
    wander_time = response.xpath('//div[@class="time"]/text()').extract_first()
    mentioned_times = response.xpath('//div[@class="countbox"]//div[@class="sum"]/text()').extract_first()
    overview = my_strip(list_to_string(response.xpath('//div[@class="e_db_content_box"]//text()').extract()))
    summery_tag = response.xpath('//div[@class="e_summary_list clrfix"]')
    address = summery_tag.xpath('//td[@class="td_l"]//span/text()').extract_first()
    open_time = summery_tag.xpath('//td[@class="td_r"]//p/text()').extract_first()
    tips = response.xpath('//div[@id="ts"]/div[2]//text()').extract()
    tips = my_strip(list_to_string(tips))
    best_time = response.xpath('//div[@id="lysj"]/div[2]//text()').extract_first()
    tickets = response.xpath('//div[@id="mp"]//p/text()').extract_first()
    comment_count = response.xpath('//span[@class="e_nav_comet_num"]//text()').extract_first()
    print("评论数：" + comment_count)
    #返回item
    item = PoispyderItem()
    item['name'] = name
    item['parent'] = parent
    item['parent_rank'] = int(parent_rank)
    item['mentioned_times'] = int(mentioned_times)
    item['overview'] = overview
    item['tickets'] = tickets
    item['address'] = address
    item['open_time'] = open_time
    item['tips'] = tips
    item['best_time'] = best_time
    item['comment_count'] = int(comment_count)
    item['wander_time'] = wander_time

    return item

class poi_spyder(scrapy.Spider):
    name = "poi"
    start_urls = ["http://travel.qunar.com/p-cs299914-beijing-jingdian-3-1"]

    def parse(self, response):

        url = response.url
        #景点详情页
        if(re.match(r"http://travel.qunar.com/p-oi", url)):
            yield parse_item(response)
        #景点列表页
        elif(re.match(r"http://travel.qunar.com/p-cs", url)):
            url_list = response.xpath('//a[@class="titlink" and @data-beacon="poi"]/@href').extract()
            for url in url_list:
                yield Request(url, callback=self.parse)
            next_page_url = response.xpath('//a[@class="page next"]/@href').extract_first()
            if(next_page_url != None):
                yield Request(next_page_url, callback=self.parse)



