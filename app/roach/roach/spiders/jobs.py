# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['https://provo.craigslist.org/search/sya']
    start_urls = ['http://https://provo.craigslist.org/search/sya/']

    def parse(self, response):
        pass
