import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

# PVeyeのURLを読み込み
url = "https://www.pveye.jp/article/news/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

# ニュースそれぞれのURLとタイトルを取得し、リスト化
elems = soup.find("div", class_ = "list news-list")
elems_news = elems.find_all("a")
url_news_list = []
title_list = []
for elem_news in elems_news:
    url_news_list.append(urljoin(url, elem_news.get("href")))
    title_list.append(elem_news.get_text(strip=True))

print(url_news_list)
print(title_list)

# 保存するcsvのパス
csv_path = "PVeye_inside_news.csv"

# csvを開いて、書き込み
with open(csv_path, 'w', newline='', encoding='utf_8_sig') as file:
    writer = csv.writer(file)
    writer.writerow(["No.", "Title", "Text"])

    # それぞれのニュースについて、ニュース本文を取得
    for i in range(len(url_news_list)):
        r_2 = requests.get(url_news_list[i])
        soup_2 = BeautifulSoup(r_2.text, "html.parser")
        elems_2 = soup_2.find("div", class_ = "entry-body")
        elems_news_2 = elems_2.find_all("p")
        news_text = ""
        for elem_news_2 in elems_news_2:
            news_text += elem_news_2.get_text(strip=True)

        writer.writerow([i+1, title_list[i], news_text])