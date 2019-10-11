
# -*- coding: utf-8 -*-
import scrapy
from ..items import RealEstateItem

class PropertySpider(scrapy.Spider):
    name = 'mainpage'
    error_counter = 0
    real_estate_link = 'https://www.immobilienscout24.de/expose/'
    data_object_ids = []

    def start_requests(self):
        urls = [
            'https://www.immobilienscout24.de/Suche/S-T/Wohnung-Kauf/Bayern/Muenchen-Kreis?enteredFrom=one_step_search',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse_real_estate_page(self, response):
        # TODO: init exposeItem
        re_item = RealEstateItem()
        re_type = response.xpath('//*[@id="is24-content"]/div[2]/div[1]/div[4]/div[1]/dl[1]/dd/text()').get()
        # ...
        yield None


    def parse(self, response):
        # TODO: get number of li-nodes inside the lu-node, instead of hardcoding 20
        for i in range(20):
            try:
                query = '//*[@id="resultListItems"]/li[%s]/div/article' % i
                resp = response.xpath(query)
                data_object_id = resp.attrib['data-obid']
                PropertySpider.data_object_ids.append(data_object_id)
            except KeyError:
                PropertySpider.error_counter += 1
                # TODO: handle errors
        
        for data_object_id in PropertySpider.data_object_ids:
            yield response.follow('expose/%s' % data_object_id, callback = self.parse_real_estate_page)

        next_page_href = response.xpath('//*[@id="pager"]/div[3]/a').attrib['href']
        if next_page_href is not None:
            yield response.follow(next_page_href, callback=self.parse)
        else:
            yield None

        # TODO: scrap next page, if it exists

    def closed(self, reason):
        print('Collected %s ids' % len(PropertySpider.data_object_ids))
        print('%s errors' % PropertySpider.error_counter)