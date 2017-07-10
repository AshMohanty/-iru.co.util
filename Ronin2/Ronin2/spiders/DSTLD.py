# -*- coding: utf-8 -*-

##Not Working

import scrapy
from scrapy import Spider
from scrapy.http import Request

class DstldSpider(scrapy.Spider):
    name = 'DSTLD'
    allowed_domains = ['dstld.com']
    start_urls = ['http://dstld.com/shop/mens/']

def parse(self, response):
    clothes = response.xpath('//*[@class="img"]/a[@class="product-link"]/@href').extract()
    for clothes in clothes:
        absolute_url = response.urljoin(clothes)
        yield Request(absolute_url, callback=self.parse_clothes)

    #proccess next page
    #next_page_url = response.xpath('//*[@id="pagination"]/a/@href').extract_first()
    #absolute_next_page_url = response.urljoin(next_page_url)
    #yield Request(absolute_next_page_url)

def parse_clothes(self, response):
    title = response.xpath('//*[@id="pdp"]/div[5]/div[2]/div[2]/div/h1/span[1]/text()').extract()
    price =  response.xpath('//*[@id="pdp"]/div[5]/div[2]/div[2]/div/h1/span[3]/span/text()').extract()
    image_url = response.xpath('//*[@class="mainimage"]/@src').extract_first()
    image_url = image_url.replace('//', 'http://')
    description = response.xpath('//*[@id="description"]/p/text()').extract()
    destination_url = response.xpath('//link[@rel="canonical"]/@href').extract()
    yield {
            'description': description,
            'destination_url': destination_url,
            'id': 0,
            'image_url': image_url,
            'price': price,
            'ranking': 0,
            'title': title
            }
