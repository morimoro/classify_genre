import requests
from bs4 import BeautifulSoup

url = "https://www.kankyo-business.jp/solar/news"

r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

print(soup)
