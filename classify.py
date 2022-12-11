#インストール
# pip install mecab-python3
#辞書インストール
# pip install unidic-lite

import MeCab
wakati = MeCab.Tagger("-Owakati")
print(wakati.parse("pythonが大好きです").split())

tagger = MeCab.Tagger()
print(tagger.parse("pythonが大好きです"))