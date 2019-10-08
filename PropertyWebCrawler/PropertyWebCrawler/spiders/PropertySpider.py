# -*- coding: utf-8 -*-
import scrapy


class PropertyspiderSpider(scrapy.Spider):
    name = 'PropertySpider'
    errors_counter = 0

    def start_requests(self):
        urls = [
            'https://www.immobilienscout24.de/Suche/S-T/Wohnung-Kauf/Bayern/Muenchen-Kreis?enteredFrom=one_step_search',

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse_ad(self, response):
        
        pass

    def parse(self, response):
        data_object_ids = []
        for i in range(20):
            try:
                query = '//*[@id="resultListItems"]/li[%s]/div/article' % i
                resp = response.xpath(query)
                data_object_id = resp.attrib['data-obid']
                data_object_ids.append(data_object_id)
            except KeyError:
                error_counter += 1

        ad_urls = ['https://www.immobilienscout24.de/expose/%s/' for data_object_id in data_object_ids]

        for ad_url in ad_urls:
            yield scrapy.Request(url=ad_url, callback=self.parse_ad)
    

        
        
        
        
        # //*[@id="result-113562767"]/div[1]/a[2]
        # //*[@id="result-113562767"]/div[1]/a[2]
        # /html/body/div[1]/div/div[2]/div/div[3]/div[1]/div[1]/div/div/ul/li[1]/div/article/div[1]/a[2]

        #//*[@id="resultListItems"]/li[2]/div
        
        
        