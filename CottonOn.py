# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class CottononSpider(scrapy.Spider):
    name = 'CottonOn'
    allowed_domains = ['cottonon.com']
    start_urls = ['http://cottonon.com/US/shop-by-category/men/']

    def parse(self, response):
        clothes = response.xpath('//a[@class="thumb-link"]/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)

        #proccess next page
        next_page_url = response.xpath('//a[@class="page-next"]/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url)

    def parse_clothes(self, response):
        title = response.css('h1::text').extract_first()
        price = response.xpath('//*[@itemprop="price"]/text()').extract()
        price = ''.join(price)
        price = price.replace('\r\n      \t\t\t\t\t', '$')
        price = price.replace('\r\n\t\t\t\t\t', '')
        image_url = response.xpath('//img[@class="productthumbnail"]/@src').extract_first()
        description = response.xpath('//*[@itemprop="description"]/text()').extract()
        description = ''.join(description)
        destination_url = response.xpath('//link[@rel="canonical"]/@href').extract_first()
        yield {
                'description': description,
                'destination_url': destination_url,
                'id': 0,
                'image_url': image_url,
                'price': price,
                'score': 0,
                'title': title
                }
