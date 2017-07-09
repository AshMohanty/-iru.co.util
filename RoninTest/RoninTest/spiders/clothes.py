# -*- coding: utf-8 -*-
import scrapy


class ClothesSpider(scrapy.Spider):
    name = 'clothes'
    allowed_domains = ['https://www.ronindivision.com/collections/frontpage']
    start_urls = ['http://www.ronindivision.com/collections/frontpage/']

    def parse(self, response):
        clothes = response.xpath('//*[@class="masonry-item product span3"]')

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
