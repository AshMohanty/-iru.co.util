# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class WindfallSpider(scrapy.Spider):
    name = 'windfall'
    allowed_domains = ['windfallclothing.com']
    start_urls = ['http://windfallclothing.com/shop/']


    def parse(self, response):
        ##get all the items urls
        clothes = response.xpath('//a[@class="woocommerce-LoopProduct-link"]/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)

        #proccess next page
        next_page_url = response.xpath('//a[@class="next page-numbers"]/@href').extract()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url)


    def parse_clothes(self, response):
        title = response.css('h1::text').extract_first()
        price = response.xpath('//*[@class="price"]/span/text()').extract_first()
        image_url =response.xpath('//*[@class="images"]/a/@href').extract()
        description = response.xpath('//*[@itemprop="description"]/p/text()').extract()
        destination_url = response.xpath('//link[@rel="canonical"]/@href').extract()
        yield {
                'description': description,
                'destination_url': destination_url,
                'id': 0,
                'image_url': image_url,
                'price': price,
                'ranking': 0,
                'title': title
                }
