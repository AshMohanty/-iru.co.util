# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class Ready2gousaSpider(scrapy.Spider):
    name = 'ready2gousa'
    allowed_domains = ['ready2gousa.com']
    start_urls = ['http://ready2gousa.com/']

    def parse(self, response):
        clothes = response.xpath('//a[contains(@href,"product/")]/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)

    def parse_clothes(self, response):
        title = response.css('h1::text').extract_first()
        price = response.css('h3::text').extract_first()
        image_url = response.xpath('//*[@id="image_1"]/img/@src').extract_first()
        description = 'Ready 2 Go Merchandise'
        destination_url = response.xpath('//link[@rel="canonical"]/@href').extract_first()

        yield {
                'description': description,
                'destinationUrl': destination_url,
                'imgUrl': image_url,
                'price': price,
                'score': 0,
                'title': title,
                'brand': 'Ready2Go'
                }
