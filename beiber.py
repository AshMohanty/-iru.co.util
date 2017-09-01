# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class BeiberSpider(scrapy.Spider):
    name = 'beiber'
    allowed_domains = ['purposetourmerch.com']
    start_urls = ['http://purposetourmerch.com/']

    def parse(self, response):
        clothes = response.xpath('//*[@class="product-container clearfix"]/a/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)



    def parse_clothes(self, response):
        title = response.css('h1::text').extract_first()
        price = response.xpath('//*[@class="currency"]/span/text()').extract_first()
        image_url = response.xpath('//*[@class="product-single__photos multi-image"]/a/@href').extract_first()
        image_url = image_url.replace('//', 'http://')
        description = 'Buggati Biebs zz'
        destination_url = response.xpath('//link[@rel="canonical"]/@href').extract_first()

        yield {
                'description': description,
                'destinationUrl': destination_url,
                'imgUrl': image_url,
                'price': price,
                'score': 0,
                'title': title,
                'sale': 'false',
                'stock': 'true',
                'brand': 'Bieber'
                }
