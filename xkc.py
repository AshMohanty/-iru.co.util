# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class XkcSpider(scrapy.Spider):
    name = 'xkc'
    allowed_domains = ['kxcstore.co.uk']
    start_urls = ['http://www.kxcstore.co.uk/category/all/']

    def parse(self, response):
        clothes = response.xpath('//*[@class="product sold span4 "]/a/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)



    def parse_clothes(self, response):
        title = response.xpath('//h3/span/text()').extract_first()
        price = response.xpath('//*[@class="price"]/span/text()').extract_first()
        image_url = response.xpath('//*[@id="product_images"]/li/a/@href').extract_first()
        description = response.xpath('//*[@id="product-desc"]/div/p[1]/text()').extract_first()
        destination_url = response.xpath('//link[@rel="canonical"]/@href').extract()

        yield {
                'description': description,
                'destinationUrl': destination_url,
                'imgUrl': image_url,
                'price': price,
                'score': 12,
                'title': title,
                'sale': 'false',
                'stock': 'true',
                'brand': 'KXC Clothing'
                }
