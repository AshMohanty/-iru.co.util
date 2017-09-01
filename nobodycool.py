# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class NobodycoolSpider(scrapy.Spider):
    name = 'nobodycool'
    allowed_domains = ['aintnobodycool.com']
    start_urls = ['http://aintnobodycool.com/']

    def parse(self, response):
        clothes = response.xpath('//*[@class="grid-product__image-wrapper"]/a/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)



    def parse_clothes(self, response):
        title = response.css('h1::text').extract_first()
        price = response.xpath('//*[@id="ProductPrice"]/text()').extract_first()
        price = price.replace('\n              ', '')
        price = price.replace('\n            ', '')
        image_url = response.xpath('//*[@class="product-single__photo-wrapper"]/img/@src').extract_first()
        image_url = image_url.replace('//', 'http://')
        description = 'Nobodys Cool'
        destination_url = response.xpath('//link[@rel="canonical"]/@href').extract_first()

        yield {
                'description': description,
                'destinationUrl': destination_url,
                'imgUrl': image_url,
                'price': price,
                'score': 0,
                'title': title,
                'brand': 'Nobody Cool'
                }
