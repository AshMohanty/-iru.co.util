# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request


class FilthytokyoSpider(scrapy.Spider):
    name = 'filthytokyo'
    allowed_domains = ['filthytokyo.myshopify.com']
    start_urls = ['http://filthytokyo.myshopify.com/collections/shop']

    def parse(self, response):
        clothes = response.xpath('//*[@class="grid__item small--one-half medium--one-half large--one-fifth"]/a/@href').extract_first()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)



    def parse_clothes(self, response):
        title = response.css('h1::text').extract_first()
        price =  response.xpath('//*[@class="product-single__prices"]/span/text()').extract_first()
        price = price.replace('\n              ', '')
        price = price.replace('\n            ', '')
        image_url = response.xpath('//img[@id="ProductPhotoImg"]/@src').extract_first()
        image_url = image_url.replace('//', 'http://')
        description = response.xpath('//ul[@class="listMCE"]/li/text()').extract_first()
        destination_url = response.xpath('//link[@rel="canonical"]/@href').extract_first()

        yield {
                'description': description,
                'destinationUrl': destination_url,
                'imgUrl': image_url,
                'price': price,
                'score': 0,
                'title': title,
                'brand': 'Filthy Tokyo'
                }
