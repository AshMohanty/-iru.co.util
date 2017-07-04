import requests
import bs4
from pprint import pprint

response = requests.get("http://www.uniqlo.com/us/men/featured/weekly-promotions.html")
soup = bs4.BeautifulSoup(response.text, "html.parser")
items = soup.select('div.product-tile-info')

def parseUniqlo(items):
	lst = []
	for item in items:

		imageUrl = item.find('div', {"class" : "product-image"}).find('a').find('img')['src'].strip()
		productName = item.find('a', {"class" : "name-link"}).text.strip()
		productPrice = item.find('span', {"class" : "product-sales-price"}).text.strip()

		name = item.findAll('a')[0].text.strip()
		newItem = {"name": productName, "price": productPrice, 
			"imageUrl" : imageUrl}

		lst += [newItem]

	return lst


pprint(parseUniqlo(items))