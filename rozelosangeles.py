# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class RozelosangelesSpider(scrapy.Spider):
    name = 'rozelosangeles'
    allowed_domains = ['rozelosangeles.bigcartel.com']
    start_urls = ['http://rozelosangeles.bigcartel.com']

    def parse(self, response):
        clothes = response.xpath('//li/a/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)


    def parse_clothes(self, response):
        title = response.css('h1::text').extract_first()
        price = response.xpath('//p/text()').extract()
        price = price[1]
        price = ''.join(price)
        price = price.replace('\n          \n        ', '')
        image_url = response.xpath('//*[@class="gallery"]/a/@href').extract_first()
        description = 'Roze Los Angeles Clothing'
        destination_url = response.xpath('//link[@rel="canonical"]/@href').extract_first()

        yield {
                'description': description,
                'destinationUrl': destination_url,
                'imgUrl': image_url,
                'price': price,
                'score': 0,
                'title': title
                }
