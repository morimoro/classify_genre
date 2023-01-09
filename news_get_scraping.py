import requests
from bs4 import BeautifulSoup

# 環境ビジネスのURLを読み込み
url = "https://www.kankyo-business.jp/solar/news"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

# divタグのクラスを指定して、ニュースそれぞれのURLを取得し、リスト化
elems = soup.find("div", class_ = "p-index__single p-index__news")
elems_news = elems.find_all("a")
url_news_list = []
for elem_news in elems_news:
    url_news_list.append(elem_news.get("href"))

# ニュースそれぞれに介してニュース本文を取得し、news_text_listに追加
news_text_list = []
for i in range(len(url_news_list)):
    r_2 = requests.get(url_news_list[i])
    soup_2 = BeautifulSoup(r_2.text, "html.parser")
    elems_2 = soup_2.find("div", class_ = "p-post__body")
    elems_news_2 = elems_2.find_all("p")
    news_text = ""
    for elem_news_2 in elems_news_2:
        news_text += elem_news_2.get_text(strip=True)
    news_text_list.append(news_text)

print(news_text_list)

import csv

csv_path = "test.csv"

with open(csv_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["No.", "Title", "Text"])
    writer.writerow([1, "Apple", 100])
    writer.writerow([2, "Banana", 200])
    writer.writerow([3, "Orange", 100])