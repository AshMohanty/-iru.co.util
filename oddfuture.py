# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class OddfutureSpider(scrapy.Spider):
    name = 'oddfuture'
    allowed_domains = ['golfwang.com']
    start_urls = ['http://golfwang.com/all-items/']

    def parse(self, response):
        clothes = response.xpath('//*[@class="ProductImage QuickView"]/a/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)


    def parse_clothes(self, response):
        title = response.css('h2::text').extract_first()
        price = response.xpath('//*[@class="ProductPrice VariationProductPrice"]/text()').extract_first()
        image_url = response.xpath('//*[@rel="prodImage"]/img/@src').extract_first()
        description = 'Odd Future Clothing'
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
                'brand': 'Odd Future'
                }
