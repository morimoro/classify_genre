# Mecabのインストール
# pip install mecab-python3
# Mecab用の辞書インストール
# pip install unidic-lite
# 参考にしたサイト
# https://qiita.com/hyo_07/items/ba3d53868b2f55ed9941

import MeCab
import os
from gensim import corpora

w_list = []
labels = []

with open('test.txt', 'r', encoding='UTF-8') as f:
    w = f.read().replace('\u3000','').replace('\n','')
    w_list.append(w)

mecab = MeCab.Tagger('mecabrc')

#形態素解析をして、名詞だけ取り出す
def tokenize(text):
    node = mecab.parseToNode(text)
    while node:
        if node.feature.split(',')[0] == '名詞':
            yield node.surface.lower()
        node = node.next

#記事群のdictについて、形態素解析をしてリストに返す
def get_words(contents):
    ret = []
    for  content in contents:
        ret.append(get_words_main(content))
    return ret

#一つの記事を形態素解析して返す
def get_words_main(content):
    return [token for token in tokenize(content)]

words = get_words(w_list)
print(words[0])

dictionary = corpora.Dictionary(words)
dictionary.filter_extremes(no_below = 200, no_above = 0.2)
#dictionary.save_as_text("./tmp/dictionary.txt") で、作成した辞書を保存可能
#dictionary = corpora.Dictionary.load_from_text("./tmp/dictionary.txt") で読み込み
courpus = [dictionary.doc2bow(word) for word in words]

print(courpus)