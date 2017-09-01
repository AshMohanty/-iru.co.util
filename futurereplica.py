# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class FuturereplicaSpider(scrapy.Spider):
    name = 'futurereplica'
    allowed_domains = ['futurereplica.com']
    start_urls = ['http://futurereplica.com/store']

    def parse(self, response):
        clothes = response.xpath('//a[contains(@href,"item")]/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)



    def parse_clothes(self, response):
        title = response.css('h1::text').extract_first()
        price = response.xpath('//*[@class="price"]/span/text()').extract_first()
        image_url = response.xpath('//*[@class="woocommerce-product-gallery__image single-product-main-image"]/a/@href').extract_first()
        description = 'Future Replica 2017 Merchandise'
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
                'brand': 'Future Replica'
                }
