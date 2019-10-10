
# -*- coding: utf-8 -*-
import scrapy
from ..items import RealEstateItem

#rename project to RealEstateScraper

class PropertySpider(scrapy.Spider):
    name = 'mainpage'
    error_counter = 0
    real_estate_link = 'https://www.immobilienscout24.de/expose/'

    def start_requests(self):
        urls = [
            'https://www.immobilienscout24.de/Suche/S-T/Wohnung-Kauf/Bayern/Muenchen-Kreis?enteredFrom=one_step_search',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse_real_estate_page(self, response):
        # TODO: init exposeItem
        realEstateItem = RealEstateItem()
        
        yield None


    def parse(self, response):
        data_object_ids = []
        # TODO: get number of li-nodes inside the lu-node, instead of hardcoding 20
        for i in range(20):
            try:
                query = '//*[@id="resultListItems"]/li[%s]/div/article' % i
                resp = response.xpath(query)
                data_object_id = resp.attrib['data-obid']
                data_object_ids.append(data_object_id)
            except KeyError:
                pass
                # TODO: handle errors
        
        for data_object_id in data_object_ids:
            next_expose = response.urljoin('/%s' % data_object_id)
            yield scrapy.Request(next_expose, callback=self.parse_real_estate_page)

        # TODO: scrap next page, if it exists
