# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class HyperdenimSpider(scrapy.Spider):
    name = 'hyperdenim'
    allowed_domains = ['hyperdenim.com']
    start_urls = ['http://hyperdenim.com/collections/bottoms']

    def parse(self, response):
        clothes = response.xpath('//*[@itemprop="itemListElement"]/a/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)

        #proccess next page
        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url)



    def parse_clothes(self, response):
        title = response.css('h1::text').extract_first()
        price = response.xpath('//*[@itemprop="price"]/span/text()').extract_first()
        price = price.replace('\n              \n                ', '')
        price = price.replace('\n              \n            ', '')
        image_url = response.xpath('//a[@class="fancybox"]/@href').extract_first()
        image_url = image_url.replace('//', 'http://')
        description = response.xpath('//*[@id="content_wrapper"]/div/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/p[2]/strong/em/b').extract_first()
        destination_url = response.xpath('//link[@rel="canonical"]/@href').extract()

        yield {
                'description': description,
                'destinationUrl': destination_url,
                'imgUrl': image_url,
                'price': price,
                'score': 0,
                'title': title,
                'sale': 'false',
                'stock': 'true',
                'brand': 'Hyper Denim'
                }
