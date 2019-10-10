# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


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
    
'''    
    def __init__(self):
        total_price             = None
        total_price             = None
        room_number             = None
        balcony                 = None
        bedroom_number          = None
        bathroom_number         = None
        property_type           = None
        garage                  = None
        internetspeed_maximum   = None
        construction_year       = None
        object_condition        = None
        heater                  = None
        power_consumption       = None
        energy_certificate      = None
        living_space            = None
        describtion             = None
'''
    