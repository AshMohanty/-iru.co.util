# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class ScrtSpider(scrapy.Spider):
    name = 'scrt'
    allowed_domains = ['scrt.onl']
    start_urls = ['http://scrt.onl/collections/all']

    def parse(self, response):
        clothes = response.xpath('//*[@class="prod_container"]/a/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)

    def parse_clothes(self, response):
        title = response.css('h1::text').extract_first()
        price = response.xpath('//*[@class="money"]/text()').extract()
        price = price[1]
        image_url = response.xpath('//*[@class="big bigimage-1 show"]/a/@href').extract_first()
        description = 'From the Scrt Only 2017 Collection'
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
                'brand': 'SCRT'
                }
