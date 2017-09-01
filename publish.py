# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class PublishSpider(scrapy.Spider):
    name = 'publish'
    allowed_domains = ['publishbrand.com']
    start_urls = ['https://publishbrand.com/all']

    def parse(self, response):
        clothes = response.xpath('//a[contains(@href,"products")]/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)



    def parse_clothes(self, response):
        title = response.xpath('//*[@class="product-title"]/text()').extract_first()
        price = response.xpath('//*[@class="price"]/text()').extract()
        price = price[1]
        price = price.replace('\n\n', '')
        price = price.replace('\n\t\t\t\t\n\t\t\t\t', '')
        image_url =  response.xpath('//*[@class="product-image"]/a/@href').extract_first()
        image_url = image_url.replace('//', 'http://')
        description = response.xpath('/html/body/div[2]/div[11]/div[3]/ul/li[2]/div/div/text()[2]').extract_first()
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
                'brand': 'publish'
                }
