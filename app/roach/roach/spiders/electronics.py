# -*- coding: utf-8 -*-
import scrapy


class ElectronicsSpider(scrapy.Spider):
    name = 'electronics'
    allowed_domains = ['https://provo.craigslist.org/search/sya']
    start_urls = ['http://https://provo.craigslist.org/search/sya/']

    def parse(self, response):
        pass
