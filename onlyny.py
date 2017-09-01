# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class OnlynySpider(scrapy.Spider):
    name = 'onlyny'
    allowed_domains = ['onlyny.com']
    start_urls = ['http://onlyny.com/collections/all-collection?page=1/']

    def parse(self, response):
        clothes = response.xpath('//*[@class="grid-image"]/a/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)

        #proccess next page
        next_page_url = response.xpath('//*[@class="icon-fallback-text"]/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url)

    def parse_clothes(self, response):
        title = response.xpath('//*[@itemprop="name"]/text()').extract_first()
        price = response.xpath('//*[@id="productPrice"]/text()').extract_first()
        price = price.replace('\n                  \n\n  \n\n\n  \n\n\n','')
        price = price.replace('\n\n                ','')
        image_url = response.xpath('//*[@class="product-photo-container zoom"]/img/@src').extract_first()
        image_url = image_url.replace('//', 'http://')
        description = response.xpath('//*[@id="tab-1"]/ul/li[3]/text()[1]').extract_first()
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
                'brand': 'OnlyNY'
                }
