# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class PharousaSpider(scrapy.Spider):
    name = 'pharousa'
    allowed_domains = ['pharousa.com']
    start_urls = ['http://pharousa.com/products']

    def parse(self, response):
        clothes = response.xpath('//*[@class="product sale"]/a/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)


    def parse_clothes(self, response):
        title = response.css('h1::text').extract_first()
        price = response.css('h4::text').extract_first()
        image_url = response.xpath('//*[@class="default_image"]/a/@href').extract_first()
        description = response.xpath('//*[@class="product_description"]/p/text()').extract_first()
        destination_url = response.xpath('//link[@rel="canonical"]/@href').extract_first()

        yield {
                'description': description,
                'destinationUrl': destination_url,
                'imgUrl': image_url,
                'price': price,
                'score': 0,
                'title': title
                }
