# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class SupremeSpider(scrapy.Spider):
    name = 'supreme'
    allowed_domains = ['supremenewyork.com']
    start_urls = ['http://supremenewyork.com/shop/all']

    def parse(self, response):
        clothes = response.xpath('//*[@class="inner-article"]/a/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)


    def parse_clothes(self, response):
        title = response.css('h1::text').extract_first()
        price = response.xpath('//*[@itemprop="price"]/text()').extract_first()
        image_url = response.xpath('//*[@itemprop="image"]/@src').extract_first()
        image_url = image_url.replace('//', 'http://')
        description = response.xpath('//*[@itemprop="description"]/text()').extract_first()
        destination_url = response.xpath('//link[@rel="canonical"]/@href').extract_first()

        yield {
                'description': description,
                'destinationUrl': destination_url,
                'imgUrl': image_url,
                'price': price,
                'score': 0,
                'title': title,
                'brand': 'Supreme'
                }
