# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class HmSpider(scrapy.Spider):
    name = 'HM'
    allowed_domains = ['hm.com']
    start_urls = ['http://www.hm.com/us/products/men?page=24']

    def parse(self, response):
        pass
