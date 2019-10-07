# -*- coding: utf-8 -*-
import scrapy


class PropertyspiderSpider(scrapy.Spider):
    name = 'PropertySpider'

    def start_requests(self):
        urls = [
            'https://www.immobilienscout24.de/Suche/S-T/Wohnung-Kauf/Bayern/Muenchen-Kreis?enteredFrom=one_step_search',

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)



    def parse(self, response):
        data_object_ids = set()
        for i in range(20):
            try:
                query = '//*[@id="resultListItems"]/li[%s]/div' % i
                resp = response.xpath(query)
                data_object_id = resp.attrib['data-obid']
                ad_links.add(data_object_id)
            except:
                print('something went wrong')

        print('------------------------------------------------------------------')
        print(data_object_ids)
        
        
        
        # //*[@id="result-113562767"]/div[1]/a[2]
        # //*[@id="result-113562767"]/div[1]/a[2]
        # /html/body/div[1]/div/div[2]/div/div[3]/div[1]/div[1]/div/div/ul/li[1]/div/article/div[1]/a[2]

        #//*[@id="resultListItems"]/li[2]/div
        
        
        