# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class ElwoodSpider(scrapy.Spider):
    name = 'Elwood'
    allowed_domains = ['elwoodclothing.com']
    start_urls = ['http://elwoodclothing.com/collections/everything/']

    def parse(self, response):
        clothes = response.xpath('//*[@class="prod-image"]/a/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)

        #proccess next page
        next_page_url = response.xpath('//*[@id="pagination"]/a[4]/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url)

    def parse_clothes(self, response):
        title = response.css('h1::text').extract_first()
        price = response.xpath('//*[@class="product-price"]/text()').extract_first()
        image_url = response.xpath('//*[@class="mainimage"]/@src').extract_first()
        image_url = image_url.replace('//', 'http://')
        description = response.xpath('//*[@id="product-description"]/div[3]/text()').extract()
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
