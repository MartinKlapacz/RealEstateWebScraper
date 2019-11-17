# -*- coding: utf-8 -*-
import scrapy
from ..items import RealEstateItem, RealEstateItemLoader
from scrapy.loader import ItemLoader
from ..xpaths import *

class RealEstateSpider(scrapy.Spider):
    name = 'mainpage'
    error_counter = 0
    item_counter = 0
    real_estate_link = 'https://www.immobilienscout24.de/expose/'
    data_ids = []

    def start_requests(self):
        urls = [
            'https://www.immobilienscout24.de/Suche/S-T/Wohnung-Kauf/Bayern/Muenchen-Kreis?enteredFrom=one_step_search',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse_real_estate_page(self, response):
        item_loader = RealEstateItemLoader(item=RealEstateItem(), response=response)
        item_loader.add_xpath('total_price', total_price_xpath)
        item_loader.add_xpath('room_number', room_number_xpath)
        item_loader.add_xpath('bedroom_number', bedroom_number_xpath)
        item_loader.add_xpath('property_type', property_type_xpath)
        item_loader.add_xpath('bedroom_number', bedroom_number_xpath)
        item_loader.add_xpath('living_space', living_space_xpath)
        item_loader.add_xpath('construction_year', construction_year_xpath)
        item_loader.add_xpath('power_consumption', power_consumption_xpath)
        item_loader.add_xpath('describtion', describtion_xpath)
        item_loader.add_xpath('internetspeed_maximum', internetspeed_maximum_xpath)
        item_loader.add_xpath('garage', garage_xpath)
        item_loader.add_xpath('energy_certificate', energy_certificate_xpath)
        RealEstateSpider.item_counter += 1
        yield item_loader.load_item()
        # causing errors:
        # item_loader.add_xpath('object_condition', object_condition_xpath)
        # item_loader.add_xpath('balcony', balcony_xpath)
        # item_loader.add_xpath('heater', heater_xpath)
        # incorrect xpaths:
        # item_loader.add_xpath('bathroom_number', bathroom_number_xpath)

    def parse(self, response):
        # TODO: get number of li-nodes inside the lu-node, instead of hardcoding 20
        i = 1
        # get all data_ids
        while i <= 20:
            li_elem = response.xpath('//*[@id="resultListItems"]/li[%s]' % i)
            li_elem_class = li_elem.attrib['class']
            if li_elem_class.strip() == 'align-center background':
                RealEstateSpider.error_counter += 1
            else:
                data_id = li_elem.attrib['data-id']
                RealEstateSpider.data_ids.append(data_id)
            i += 1

        # crawl each data_id website
        for data_id in RealEstateSpider.data_ids:
            yield scrapy.Request(url='https://www.immobilienscout24.de/expose/%s#/' % data_id, callback = self.parse_real_estate_page)
        RealEstateSpider.data_ids.clear()

        # go to next feed page if it exists
        next_page_href = response.xpath('//*[@id="pager"]/div[3]/a').attrib['href']
        if next_page_href is not None:
            yield response.follow(next_page_href, callback=self.parse)
        else:
            yield None

    def closed(self, reason):
        print('Collected ids: %s' % RealEstateSpider.item_counter)
        print('Error ids: %s' % RealEstateSpider.error_counter)