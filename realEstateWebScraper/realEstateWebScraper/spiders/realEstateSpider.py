# -*- coding: utf-8 -*-
import scrapy
from ..items import RealEstateItem
from scrapy.loader import ItemLoader

class RealEstateSpider(scrapy.Spider):
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
        loader = ItemLoader(item=RealEstateItem(), response=response)

        loader.add_xpath('total_price', '//*[@id="is24-content"]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]')
        loader.add_xpath('room_number', '//*[@id="is24-content"]/div[2]/div[1]/div[4]/div[1]/dl[4]/dd')
        loader.add_xpath('bedroom_number', '//*[@id="is24-content"]/div[2]/div[1]/div[4]/div[1]/dl[5]/dd')

        loader.add_xpath('bathroom_number', '//*[@id="is24-content"]/div[2]/div[1]/div[4]/div[1]/dl[6]/dd')
        
        loader.add_xpath('', '')
        loader.add_xpath('', '')
        loader.add_xpath('', '')
        loader.add_xpath('', '')
        loader.add_xpath('', '')
        loader.add_xpath('', '')
        loader.add_xpath('', '')
        loader.add_xpath('', '')
        loader.add_xpath('', '')
        loader.add_xpath('', '')
        loader.add_xpath('', '')
        loader.add_xpath('', '')
        loader.add_xpath('', '')
        loader.add_xpath('', '')
        loader.add_xpath('', '')

        item = response.xpath('//*[@id="is24-content"]/div[2]/div[1]/div[4]/div[1]/dl[1]/dd/text()').get() 
        
        yield None

    def parse(self, response):
        # TODO: get number of li-nodes inside the lu-node, instead of hardcoding 20
        i = 1
        while i <= 20:
            if response.xpath('//*[@id="resultListItems"]/li[%s]' % i).attrib['class'].strip() == 'align-center background':
                RealEstateSpider.error_counter += 1
                i += 1
            else:
                query = '//*[@id="resultListItems"]/li[%s]/div/article' % i
                resp = response.xpath(query)
                data_object_id = resp.attrib['data-obid']
                RealEstateSpider.data_object_ids.append(data_object_id)
                i += 1

        for data_object_id in RealEstateSpider.data_object_ids:
            yield response.follow('expose/%s' % data_object_id, callback = self.parse_real_estate_page)

        next_page_href = response.xpath('//*[@id="pager"]/div[3]/a').attrib['href']
        if next_page_href is not None:
            yield response.follow(next_page_href, callback=self.parse)
        else:
            yield None


    def closed(self, reason):
        print('Collected %s ids' % len(RealEstateSpider.data_object_ids))
        print(RealEstateSpider.error_counter)
        

        '''
total_price             
total_price             
room_number             
balcony                 
bedroom_number          
bathroom_number         
property_type           
garage                  
internetspeed_maximum   
construction_year       
object_condition        
heater                  
power_consumption       
energy_certificate      
living_space            
describtion             
'''
