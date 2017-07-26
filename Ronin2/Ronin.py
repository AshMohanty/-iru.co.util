# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class RoninSpider(scrapy.Spider):
    name = 'Ronin'
    allowed_domains = ['ronindivision.com']
    start_urls = ['http://ronindivision.com/collections/frontpage/']

    def parse(self, response):
        clothes = response.xpath('//*[@class="image"]/a/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)

        #proccess next page
        next_page_url = response.xpath('//*[@class="item link"]/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url)

    def parse_clothes(self, response):
        title = response.css('h1::text').extract_first()
        price = response.xpath('//*[@class="price"]/text()').extract_first()
        image_url = response.xpath('//*[@class="image featured"]/a/@href').extract_first()
        image_url = image_url.replace('//', 'http://')
        description = response.xpath('//*[@class="description"]/p/text()').extract_first()
        destination_url = response.xpath('//link[@rel="canonical"]/@href').extract_first()
        yield {
                'description': description,
                'destinationUrl': destination_url,
                'imgUrl': image_url,
                'price': price,
                'ranking': 0,
                'title': title
                }
