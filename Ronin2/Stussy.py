# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request


class StussySpider(scrapy.Spider):
    name = 'Stussy'
    allowed_domains = ['stussy.com']
    start_urls = ['http://stussy.com/us/mens/new-arrivals/',
                  'http://stussy.com/us/mens/tees'

                 ]

    def parse(self, response):
        clothes = response.xpath('//*[@class="product-inner"]/a/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)

        #proccess next page
        ##next_page_url = response.xpath('//*[@class="item link"]/@href').extract_first()
        ##absolute_next_page_url = response.urljoin(next_page_url)
        ##yield Request(absolute_next_page_url)

    def parse_clothes(self, response):
        title = response.xpath('//*[@class="product-name"]/h1/text()').extract_first()
        price = response.xpath('//*[@class="price"]/text()').extract()
        image_url = response.xpath('//img/@src').extract_first()
        ##image_url = image_url.replace('//', 'http://')
        description = response.xpath('//*[@class="std product-view-info product-view-display"]/ul/li/text()').extract()
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
