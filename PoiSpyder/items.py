# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PoispyderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    name = scrapy.Field()
    parent = scrapy.Field()
    parent_rank = scrapy.Field()
    mentioned_times = scrapy.Field()
    overview = scrapy.Field()
    tickets = scrapy.Field()
    address = scrapy.Field()
    open_time = scrapy.Field()
    tips = scrapy.Field()
    best_time = scrapy.Field()
    comment_count = scrapy.Field()
    wander_time = scrapy.Field()
