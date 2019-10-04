# -*- coding: utf-8 -*-
import scrapy


class PropertyspiderSpider(scrapy.Spider):
    name = 'PropertySpider'
    allowed_domains = ['https://www.immobilienscout24.de/Suche/S-T/Wohnung-Kauf/Bayern/Muenchen-Kreis?enteredFrom=one_step_search']
    start_urls = ['http://https://www.immobilienscout24.de/Suche/S-T/Wohnung-Kauf/Bayern/Muenchen-Kreis?enteredFrom=one_step_search/']

    def parse(self, response):
        pass
