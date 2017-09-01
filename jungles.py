# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class JunglesSpider(scrapy.Spider):
    name = 'jungles'
    allowed_domains = ['junglesjungles.com']
    start_urls = ['http://junglesjungles.com/collections/all']

    def parse(self, response):
        clothes = response.xpath('//a[contains(@href,"products")]/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)

        #proccess next page
        next_page_url = response.xpath('//*[@id="PageContainer"]/main/div[2]/span[4]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url)

    def parse_clothes(self, response):
        title = response.css('h2::text').extract_first()
        price = response.xpath('//*[@class="product__price--reg js-price"]/text()').extract_first()
        price = price.replace('\n                  ','')
        price = price.replace('\n                ', '')
        image_url = response.xpath('//*[@class="product__photo grid__item medium-up--one-half"]/img/@src').extract_first()
        image_url = image_url.replace('//', 'http://')
        description = 'Jungles Jungles 2017 Merchandise'
        destination_url = response.xpath('//link[@rel="canonical"]/@href').extract_first()

        yield {
                'description': description,
                'destinationUrl': destination_url,
                'imgUrl': image_url,
                'price': price,
                'score': 0,
                'title': title,
                'brand': 'Jungles Jungles'
                }
