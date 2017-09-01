# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class HelascapsSpider(scrapy.Spider):
    name = 'helascaps'
    allowed_domains = ['helascaps.com']
    start_urls = ['http://store.helascaps.com/']

    def parse(self, response):
        clothes = response.xpath('//a[@class="product_img_link"]/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)



    def parse_clothes(self, response):
        title = response.css('h1::text').extract_first()
        price = response.xpath('//*[@class="price"]/text()').extract_first()
        image_url = response.xpath('//*[@class="product-single__photos"]/img/@src').extract_first()
        description = 'Helascaps 2017'
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
                'brand': 'Helascaps'
                }
