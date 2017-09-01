# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class PalaceSpider(scrapy.Spider):
    name = 'palace'
    allowed_domains = ['palaceskateboards.com']
    start_urls = ['http://shop-usa.palaceskateboards.com']

    def parse(self, response):
        clothes = response.xpath('//*[@class="product-grid-item clearfix"]/a/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)

    def parse_clothes(self, response):
        title = response.css('h1::text').extract_first()
        price = '~$200'
        image_url = response.xpath('//a[contains(@href,"cdn")]/@href').extract_first()
        image_url = image_url.replace('//', 'http://')
        description = response.xpath('//*[@class="product-text"]/ul/li/text()').extract()
        description = ''.join(description)
        destination_url = response.xpath('//link[@rel="canonical"]/@href').extract_first()

        yield {
                'description': description,
                'destinationUrl': destination_url,
                'imgUrl': image_url,
                'price': price,
                'score': 0,
                'title': title,
                'sale': 'false',
                'stock': 'false',
                'brand': 'Palace'
                }
