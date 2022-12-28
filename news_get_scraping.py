import requests
from bs4 import BeautifulSoup

# 環境ビジネスのURLを読み込み
url = "https://www.kankyo-business.jp/solar/news"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

# divタグのクラスを指定して、ニュース一つ分のURLを取得
elems = soup.find("div", class_ = "p-index__single p-index__news")
elems_news = elems.find_all("a")
url_news_list = []
for elem_news in elems_news:
    url_news_list.append(elem_news.get("href"))

r_2 = requests.get(url_news_list[0])
soup_2 = BeautifulSoup(r_2.text, "html.parser")

elems_2 = soup_2.find("div", class_ = "p-post__body")
elems_news_2 = elems_2.find_all("p")

newslist = ""
for elem_news_2 in elems_news_2:
    newslist += elem_news_2.get_text(strip=True)

print(newslist)
