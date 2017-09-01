# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class WetstoreSpider(scrapy.Spider):
    name = 'wetstore'
    allowed_domains = ['wetstore.jp']
    start_urls = ['http://wetstore.jp/store']

    def parse(self, response):
        clothes = response.xpath('//li[@class="product"]/a/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)



    def parse_clothes(self, response):
        title = response.css('h1::text').extract_first()
        price =  response.xpath('//*[@class="detail"]/p/text()').extract()
        price = ''.join(price)
        price = price.replace('\n          ','')
        price = price.replace('\n          \n            ', '')
        price = price.replace('\n          \n        ', '')
        image_url = response.xpath('//*[@class="gallery"]/a/@href').extract_first()
        description = response.xpath('//*[@class="description"]/p/text()').extract_first()
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
                'brand': 'Wet Store'
                }
