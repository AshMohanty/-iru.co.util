Things you'll need to scrape:
Python3
Scrapy
VirtualEnv

To install Scrapy(https://scrapy.org/):  
pip install scrapy   

To install VirtualEvn(https://virtualenv.pypa.io):
pip install virtualenv


To run:
scrapy runspider uniqlo_shirts.py  ///NOT WORKING RIGHT NOW

It will return a JSON in CARD format. 


We will start using Scrapy cloud soon and the key for our instance is(        ). 

Yeild feild is how the JSON is returned:
    yield {
            'description': description,
            'destination_url': destination_url,
            'id': idd,
            'image_url': image_url,
            'price': price,
            'ranking': 0,
            'title': title
        }

