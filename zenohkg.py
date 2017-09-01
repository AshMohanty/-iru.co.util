# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request


class ZenohkgSpider(scrapy.Spider):
    name = 'zenohkg'
    allowed_domains = ['zenohkg.com']
    start_urls = ['http://zenohkg.com/collections/t-shirts/']

    def parse(self, response):
        clothes = response.xpath('//*[@itemprop="itemListElement"]/a/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)



    def parse_clothes(self, response):
        title = response.css('h1::text').extract_first()
        price = '$40'
        image_url = response.xpath('//*[@id="product-9648787203-gallery"]/ul/li[2]/a/@href').extract_first()
        description = response.xpath('//*[@id="content_wrapper"]/div[4]/div[2]/div[1]/div/div[2]/div[1]/p[1]/span/text()').extract_first()
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
                'brand': 'Zeno Hong Kong'
                }
