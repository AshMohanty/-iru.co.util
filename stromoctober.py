# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class StromoctoberSpider(scrapy.Spider):
    name = 'stromoctober'
    allowed_domains = ['stromoctober.com']
    start_urls = ['http://stromoctober.com/']


    def parse(self, response):
        clothes = response.xpath('//a[contains(@href,"product/")]/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)


    def parse_clothes(self, response):
        title = response.css('h1::text').extract_first()
        price = response.css('h3::text').extract()
        price = price[1]
        image_url = response.xpath('//li/img/@src').extract_first()
        description = response.xpath('//*[@class="product_description"]/p/text()').extract_first()
        destination_url = response.xpath('//link[@rel="canonical"]/@href').extract()

        yield {
                'description': description,
                'destinationUrl': destination_url,
                'imgUrl': image_url,
                'price': price,
                'score': 0,
                'title': title,
                'sale': 'false',
                'stock': 'true',
                'brand': 'StromOctober'
                }
