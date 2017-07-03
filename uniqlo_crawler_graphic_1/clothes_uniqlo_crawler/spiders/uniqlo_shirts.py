from scrapy import Spider
from scrapy.http import Request


def product_info(response, value):
    return response.xpath('//th[text()="' + value + '"]/following-sibling::td/text()').extract_first()


class ShirtsSpider(Spider):
    name = 'shirts'
    allowed_domains = ['https://www.uniqlo.com/us/en/men/ut-graphic-tees']
    start_urls = ['https://www.uniqlo.com/us/en/men/ut-graphic-tees']

    def parse(self, response):
        shirts = response.xpath('//h3/a/@href').extract()
        for shirt in shirts:
            absolute_url = response.urljoin(graphicshirt)
            yield Request(absolute_url, callback=self.parse_shirt)

        # processing of the next page but not working
        #next_page_url = response.xpath('//a[text()="next"]/@href').extract_first()
        #absolute_next_page_url = response.urljoin(next_page_url)
        #yield Request(absolute_next_page_url)



    def parse_shirt(self, response):
        title = response.css('h1::text').extract_first()
        price = response.xpath('//*[@class="price_color"]/text()').extract_first()

        image_url = response.xpath('//img/@src').extract_first()
        destination_url = response.xpath('//@src.shop'.extract_first()


        description = response.xpath(
            '//*[@id="product_description"]/following-sibling::p/text()').extract_first()

        idd = randrange(0, 1000000)

        yield {
            'description': description,
            'destination_url': destination_url,
            'id': idd,
            'image_url': image_url,
            'price': price,
            'ranking': 0,
            'title': title
        }
