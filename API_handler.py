import requests
from bs4 import BeautifulSoup


class ProductHandler():
    def __init__(self):
        self.url = "https://www.s-kaupat.fi/tuote/"

    def get_response(self, ean_code):
        query_url = self.url + ean_code
        response = requests.get(query_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        element = soup.find(attrs={'data-test-id': 'product-name'})
        element_img = soup.find(attrs={'alt': element.text, "loading": "lazy"}).get("src")
        print(element_img)
        return element.text

