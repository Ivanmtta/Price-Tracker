import requests
from bs4 import BeautifulSoup

class Web_Scraper:

  def __init__(self):
    self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}

  def scrape_page(self, soup, amazon_link):
    name = soup.find(id = 'productTitle').get_text().strip()
    image = soup.find(id = 'imgTagWrapperId').img.get('data-a-dynamic-image').split('"')[1]
    try:
      original_price = float(soup.find(id = 'priceblock_ourprice').get_text()[1:])
    except:
      original_price = float(soup.find(id = 'priceblock_dealprice').get_text()[1:])
    return {
      'name': name,
      'image': image,
      'original_price': original_price,
      'current_price': original_price,
      'url': amazon_link
    }

  def get_item(self, amazon_link):
    web_page = requests.get(amazon_link, headers = self.headers)
    soup = BeautifulSoup(web_page.content, 'html5lib')
    return self.scrape_page(soup, amazon_link)

  def update_price(self, amazon_link, original_price):
    web_page = requests.get(amazon_link, headers = self.headers)
    soup = BeautifulSoup(web_page.content, 'html5lib')
    try:
      new_price = float(soup.find(id = 'priceblock_ourprice').get_text()[1:])
    except:
      new_price = float(soup.find(id = 'priceblock_dealprice').get_text()[1:])
    return new_price