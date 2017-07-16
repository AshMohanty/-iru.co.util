# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request


class UoSpider(scrapy.Spider):
    name = 'UO'
    allowed_domains = ['urbanoutfitters.com']
    start_urls = ['http://urbanoutfitters.com/mens-back-in-stock/']

    def parse(self, response):
        clothes = response.xpath('//*[@class="c-product-tile-controls__link-wrap js-product-tile-controls__link-wrap"]/a/@href').extract()
        for clothes in clothes:
            absolute_url = response.urljoin(clothes)
            yield Request(absolute_url, callback=self.parse_clothes)

        #proccess next page
        next_page_url = response.xpath('//*[@class="o-pagination__li o-pagination__li--arrow"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url)

    def parse_clothes(self, response):
        title = response.xpath('//*[@class="c-product-meta__h1 u-small--show"]/span/text()').extract()
        price = response.xpath('//*[@class="c-product-meta__current-price"]/text()')[-1].extract()
        image_url = response.xpath('//*[@class="o-carousel__flex-wrapper"]/img/@src').extract_first()
        image_url = image_url.replace('//', 'http://')
        description = response.xpath('//*[@class="u-global-p"]/p/text()').extract()
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
