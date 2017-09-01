# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class OnemethSpider(scrapy.Spider):
    name = 'onemeth'
    allowed_domains = ['onemeth.com']
    start_urls = ['http://onemeth.com/collections/ss16-1']

    def parse(self, response):
        clothes = response.xpath('//a[contains(@href,"products")]/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)



    def parse_clothes(self, response):
        title = response.css('h1::text').extract_first()
        price = response.xpath('//*[@class="money"]/text()').extract()
        price = price[2]
        image_url = response.xpath('//a[@class="photo"]/@href').extract_first()
        image_url = image_url.replace('//', 'http://')
        description = response.xpath('/html/body/section/article/div[2]/div[1]/p[1]/text()').extract_first()
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
                'brand': 'One Meth'
                }
