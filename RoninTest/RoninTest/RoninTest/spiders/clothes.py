# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy import Spider


class ClothesSpider(scrapy.Spider):
    name = 'clothes'
    allowed_domains = ['ronindivision.com']
    start_urls = ['http://www.ronindivision.com/collections/frontpage?page=1']

    def parse(self, response):
        clothes = response.xpath('//*[@class="masonry-item product span3"]')


        for clothes in clothes:

            destinationlink = clothes.xpath(
                './/*[@class="image"]/a/@href').extract()

            imgurl = clothes.xpath(
                './/*[@class="image"]/a/img/@src').extract()

            title = clothes.xpath(
                './/*[@class="image"]/a/img/@alt').extract()

            yield {
                'description': '',
                'destination_url': destinationlink,
                'id': 0,
                'image_url': imgurl,
                'price': 0,
                'ranking': 0,
                'title': title
        }
        next_page_url = response.xpath(
            '//*[@class="parts"]/a/@href').extract()

        absolute_next_page_url = 'http://www.ronindivision.com/collections/frontpage?page=2'

        yield Request(absolute_next_page_url, callback=self.parse)
