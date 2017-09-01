# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class WckdSpider(scrapy.Spider):
    name = 'wckd'
    allowed_domains = ['wckdthghts.com']
    start_urls = ['http://wckdthghts.com/shop']

    def parse(self, response):
        clothes = response.xpath('//a[@class="productlist-item-link"]/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)

    def parse_clothes(self, response):
        title = response.xpath('//*[@class="productitem-title"]/text()').extract_first()
        price = response.xpath('//*[@class="sqs-money-native"]/text()').extract_first()
        image_url = response.xpath('//img[contains(@src,"square")]/@src').extract_first()
        image_url = image_url.replace('//', 'http://')
        description = response.xpath('//p/text()').extract_first()
        destination_url = response.xpath('//link[@rel="canonical"]/@href').extract_first()

        yield {
                'description': description,
                'destinationUrl': destination_url,
                'imgUrl': image_url,
                'price': price,
                'score': 0,
                'title': title,
                'brand': 'Wicked Thoughts'
                }
