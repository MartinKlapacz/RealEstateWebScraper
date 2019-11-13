# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join


class RealEstateItem(scrapy.Item):
    total_price = scrapy.Field()
    room_number = scrapy.Field()
    balcony = scrapy.Field()
    bedroom_number = scrapy.Field()
    bathroom_number = scrapy.Field()
    property_type = scrapy.Field()
    garage = scrapy.Field()
    internetspeed_maximum = scrapy.Field()
    construction_year = scrapy.Field()
    object_condition = scrapy.Field()
    heater = scrapy.Field()
    power_consumption = scrapy.Field()
    energy_certificate = scrapy.Field()
    living_space = scrapy.Field()
    describtion = scrapy.Field()

class RealEstateItemLoader(ItemLoader):
    default_input_processor = TakeFirst()