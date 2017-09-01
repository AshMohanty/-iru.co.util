# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request


class StussySpider(scrapy.Spider):
    name = 'Stussy'
    allowed_domains = ['stussy.com']
    start_urls = ['http://www.stussy.com/us/mens/tees'
                  ]

    def parse(self, response):
        clothes = response.xpath('//*[@class="product-inner"]/a/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)
            yield Request('http://stussy.com/us/mens/new-arrivals', callback=self.parse_clothes)



    def parse_clothes(self, response):
        title = response.xpath('//*[@class="product-name"]/h1/text()').extract_first()
        price = response.xpath('//*[@class="price"]/text()').extract_first()
        image_url = response.xpath('//img/@src').extract_first()
        ##image_url = image_url.replace('//', 'http://')
        description = response.xpath('//*[@class="std product-view-info product-view-display"]/ul/li/text()').extract()
        description = ''.join(description)
        destination_url = response.xpath('//link[@rel="canonical"]/@href').extract_first()
        yield {
                'description': description,
                'destinationUrl': destination_url,
                'id': 0,
                'imgUrl': image_url,
                'score': price,
                'ranking': 0,
                'title': title,
                'brand': 'Stussy'
                }
